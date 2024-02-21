package third

import (
	"context"
	"fmt"
)

func (s *Usecase) GetInterestedPartnersByIds(ctx context.Context, itemIDs []external.ItemID) (map[internal.AgencyID]contracts.InterestedPartner, error) {
	results := map[internal.AgencyID]contracts.InterestedPartner{}

	items, err := s.itemGateway.BulkGet(ctx, itemIDs)
	if err != nil {
		return nil, fmt.Errorf("error getting items: %w", err)
	}

	itemsMap := make(map[external.ItemID]*itemGateway.Item)
	for _, item := range items {
		itemsMap[item.ID] = item
	}

	for _, itemID := range itemIDs {
		item, ok := itemsMap[itemID]
		if !ok {
			ctx = s.logger.WithFields(ctx, map[string]interface{}{
				"item_id": itemID,
				"method":  "get_interested_partners_by_ids",
			})
			s.logger.Error(ctx, "get item by id from gateway")

			continue
		}

		var coords *model.Coordinates
		if item.Latitude != nil && item.Longitude != nil {
			coords = &model.Coordinates{
				Latitude:  *item.Latitude,
				Longitude: *item.Longitude,
			}
		}

		partnerFilters, err := s.filters.FindSuitablePartnerFilters(ctx, &filters.SuitablePartnerFiltersSpecification{
			Price: item.Price,
			Address: model.Address{
				GeoID:       &item.LocationID,
				Coordinates: coords,
			},
			Category: model.CategoryInformation{
				Category:   item.CategoryID,
				ObjectType: item.ObjectType,
			},
		})
		if err != nil {
			return nil, fmt.Errorf("find suitable partner filters: %w", err)
		}

		for _, partnerFilter := range partnerFilters {
			partner, ok := results[partnerFilter.AgencyBillingInfo.AgencyID]
			if !ok {
				balanceType, balance, err := s.getBalanceAndBalanceType(ctx, partnerFilter.AgencyBillingInfo)
				if err != nil {
					return nil, fmt.Errorf("get balance and balance type: %w", err)
				}

				partner = contracts.InterestedPartner{
					Balance:     balance,
					BalanceType: balanceType,
					Filters:     map[int64]contracts.InterestedPartnerFilter{},
				}
			}

			filter, ok := partner.Filters[partnerFilter.ID]
			if !ok {
				filter = contracts.InterestedPartnerFilter{
					LeadsPerDay: int(partnerFilter.DesiredAttachedLeads),
				}
			}

			filter.InterestedInItems = append(filter.InterestedInItems, itemID)
			partner.Filters[partnerFilter.ID] = filter
			results[partnerFilter.AgencyBillingInfo.AgencyID] = partner
		}
	}

	return results, nil
}
