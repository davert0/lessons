package example1

import (
	"context"
	"fmt"
)

var inStatuses = []string{
	premier_partner.DealStatus_SOLD,
	premier_partner.DealStatus_REFUSED_BY_SELLER,
}

type (
	AggregatedUserDetails struct {
		ID       external.UserID
		Name     string
		ImageURL map[string]string
	}

	Usecase struct {
		deals     deals.Gateway
		users     users.Gateway
		avatars   avatars.Gateway
		items     items.Gateway
		converter Converter
	}

	determinedDetails struct {
		userDetails map[external.UserID]AggregatedUserDetails
		itemDetails map[external.ItemID]items.Details
	}
)

func New(
	deals deals.Gateway,
	users users.Gateway,
	avatars avatars.Gateway,
	items items.Gateway,
	converter Converter,
) *Usecase {
	return &Usecase{
		deals:     deals,
		users:     users,
		avatars:   avatars,
		items:     items,
		converter: converter,
	}
}

func (u *Usecase) Handle(
	ctx security.Context, in *contracts.AgentRoomArchivedDealsIn, request pageable.Request[sort.GetDeals],
) (pageable.Page[contracts.ArchivedDeal], error) {
	spec := &deals.GetDealsSpec{
		WithMember: []external.UserID{in.UserID},
		InStatuses: inStatuses,
	}

	page, err := u.deals.GetDealsBySpec(ctx, spec, request)
	if err != nil {
		return nil, err
	}

	details, err := u.determinerDetails(ctx, page)
	if err != nil {
		return nil, err
	}

	return pageable.Map(page, u.ConvertArchivedDeal(details.userDetails, details.itemDetails))
}

func (u *Usecase) determinerDetails(
	ctx context.Context,
	page pageable.Page[deals.Deal],
) (*determinedDetails, error) {
	if len(page.Elements()) == 0 {
		return &determinedDetails{}, nil
	}

	userIDs := make([]external.UserID, 0)
	itemIDs := make([]external.ItemID, 0)
	for _, element := range page.Elements() {
		for _, member := range element.Team {
			if member.Role != dictionaries.DealTeamMemberRoleAgent &&
				member.Role != dictionaries.DealTeamMemberRoleSeller {
				continue
			}
			userIDs = append(userIDs, member.ID)
		}

		agentItemID := element.RealtyObject.AgentItemID
		if agentItemID != nil {
			itemIDs = append(itemIDs, *agentItemID)
		}

		sellerItemID := element.RealtyObject.SellerItemID
		if sellerItemID != nil {
			itemIDs = append(itemIDs, *sellerItemID)
		}
	}

	group, groupCtx := errgroup.WithContext(ctx)

	var userDetails map[external.UserID]users.Details
	group.Go(func() error {
		var err error
		userDetails, err = u.users.GetAll(groupCtx, userIDs...)
		return err
	})

	var avatarDetails map[external.UserID]avatars.Details
	group.Go(func() error {
		var err error
		avatarDetails, err = u.avatars.GetDetailsByUserIDs(groupCtx, userIDs...)
		return err
	})

	var itemDetails map[external.ItemID]items.Details
	if len(itemIDs) > 0 {
		group.Go(func() error {
			var err error
			itemDetails, err = u.items.GetAll(groupCtx, itemIDs...)
			return err
		})
	}

	if err := group.Wait(); err != nil {
		return &determinedDetails{}, err
	}

	aggregatedUserDetails, err := u.aggregateUserDetails(userDetails, avatarDetails)
	if err != nil {
		return nil, err
	}

	return &determinedDetails{aggregatedUserDetails, itemDetails}, nil
}

func (u *Usecase) aggregateUserDetails(
	users map[external.UserID]users.Details,
	avatars map[external.UserID]avatars.Details,
) (map[external.UserID]AggregatedUserDetails, error) {
	aggregatedDetailsMap := make(map[external.UserID]AggregatedUserDetails)
	for id, userDetails := range users {
		if _, exists := aggregatedDetailsMap[id]; !exists {
			aggregatedDetailsMap[id] = AggregatedUserDetails{ID: id}
		}
		aggregated := aggregatedDetailsMap[id]
		aggregated.Name = userDetails.Name
		aggregatedDetailsMap[id] = aggregated
	}

	for id, avatarDetails := range avatars {
		if _, exists := aggregatedDetailsMap[id]; !exists {
			aggregatedDetailsMap[id] = AggregatedUserDetails{ID: id}
		}
		aggregated := aggregatedDetailsMap[id]
		aggregated.ImageURL = avatarDetails.ImageURL
		aggregatedDetailsMap[id] = aggregated
	}

	return aggregatedDetailsMap, nil
}

func (u *Usecase) ConvertArchivedDeal(
	userDetails map[external.UserID]AggregatedUserDetails,
	itemDetails map[external.ItemID]items.Details,
) func(deal deals.Deal) (contracts.ArchivedDeal, error) {
	return func(deal deals.Deal) (contracts.ArchivedDeal, error) {
		var clientDetails *contracts.ClientDetails
		for _, member := range deal.Team {
			if member.Role == dictionaries.DealTeamMemberRoleSeller {
				details, ok := userDetails[member.ID]
				if !ok {
					return contracts.ArchivedDeal{}, fmt.Errorf("details absent by '%d' user", member.ID)
				}
				clientDetails = &contracts.ClientDetails{
					Name:  details.Name,
					Image: details.ImageURL,
				}
			}
		}

		if clientDetails == nil {
			return contracts.ArchivedDeal{}, fmt.Errorf("seller is absent in team")
		}

		sellerItemID := deal.RealtyObject.SellerItemID
		var sellerItem *contracts.ItemDetails
		switch {
		case sellerItemID != nil:
			item, ok := itemDetails[*sellerItemID]
			if !ok {
				return contracts.ArchivedDeal{}, fmt.Errorf("details are absent by '%d' item", *sellerItemID)
			}

			details := u.converter.ConvertItemDetails(item)
			sellerItem = &details
		case deal.RealtyObject.SellerObject != nil:
			details := u.converter.ConvertObjectDetails(*deal.RealtyObject.SellerObject)
			sellerItem = &details
		}

		stage, err := mapper.ConvertStatusToStage(deal.Status.Status)
		if err != nil {
			return contracts.ArchivedDeal{}, err
		}
		dealRequest := contracts.ArchivedDeal{
			ID:           deal.ID,
			Stage:        stage,
			Type:         dictionaries.ProcessTypeComfortDeal,
			Client:       *clientDetails,
			RealtyObject: *sellerItem,
		}
		return dealRequest, nil
	}
}
