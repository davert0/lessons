package example1

import "fmt"

var inStatuses = []string{
	premier_partner.DealStatus_SOLD,
	premier_partner.DealStatus_REFUSED_BY_SELLER,
}

type (
	Usecase struct {
		deals      deals.Gateway
		determiner dealscomposer.Determiner
		converter  Converter
	}
)

func New(
	deals deals.Gateway,
	determiner dealscomposer.Determiner,
	converter Converter,
) *Usecase {
	return &Usecase{
		deals:      deals,
		determiner: determiner,
		converter:  converter,
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

	userIDs := dealscomposer.ExtractUserIDsFromDeal(page)
	itemIDs := dealscomposer.ExtractItemIDsFromDeal(page)

	userDetails, err := u.determiner.DetermineUserDetails(ctx, userIDs)
	if err != nil {
		return nil, err
	}

	itemDetails, err := u.determiner.DetermineItemDetails(ctx, itemIDs)
	if err != nil {
		return nil, err
	}

	return pageable.Map(page, u.ComposeArchivedDeal(userDetails, itemDetails))
}

func (u *Usecase) ComposeArchivedDeal(
	userDetails map[external.UserID]contracts.AggregatedUserDetails,
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

		stage, err := dealscomposer.ConvertStatusToStage(deal.Status.Status)
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
