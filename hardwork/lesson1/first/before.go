package first

import (
	"context"
	"errors"
	"fmt"
)

func (d *DefaultService) ExtractItemInfoFromAgencyLeads(ctx context.Context, agencyLeads ...model.AgencyLead) (map[internal.AgencyLeadID]model.AgencyLeadItemInfo, error) {
	itemIDs := make([]external.ItemID, 0, len(agencyLeads))
	for _, agencyLead := range agencyLeads {
		if agencyLead.ItemID != nil {
			itemIDs = append(itemIDs, *agencyLead.ItemID)
		}
	}
	items, err := d.fetchItems(ctx, itemIDs)
	if err != nil && !errors.Is(err, errEmptyItems) {
		return nil, fmt.Errorf("fetch items: %w", err)
	}

	itemInfos := make(map[internal.AgencyLeadID]model.AgencyLeadItemInfo, len(agencyLeads))
	for _, agencyLead := range agencyLeads {
		var itemInfo *model.AgencyLeadItemInfo
		// Если присутствует item_id объявления АН, тогда извлекаем из него информацию, иначе считаем его недоступным и берем информацию из атрибутов
		if agencyLead.ItemID != nil {
			item, ok := items[*agencyLead.ItemID]
			if ok {
				var address string
				if item.Address != nil {
					address = *item.Address
				}

				imagePath := d.getImageUrlByID(ctx, agencyLead.ID, item.ImageID)
				deeplink := d.makeDeeplink(ctx, item.ID)
				itemInfo = &model.AgencyLeadItemInfo{
					Title:        item.Title,
					Price:        item.Price,
					Address:      address,
					UrlPath:      item.Link,
					ImagePath:    imagePath,
					IsAgencyItem: true,
					Deeplink:     deeplink,
				}
			} else {
				d.logger.Warning(ctx, fmt.Sprintf("could not fetch item id '%d' for agency lead id '%d'. Falling back to attributes",
					*agencyLead.ItemID, agencyLead.ID))
			}
		}

		if itemInfo != nil {
			itemInfos[agencyLead.ID] = *itemInfo
			continue
		}

		address := ""
		if agencyLead.Attributes.AddressString != nil {
			address = *agencyLead.Attributes.AddressString
		}

		imagePath := d.getImageUrlByID(ctx, agencyLead.ID, agencyLead.Attributes.ImageID)
		itemInfos[agencyLead.ID] = model.AgencyLeadItemInfo{
			Title:        agencyLead.Attributes.Title,
			Price:        agencyLead.Attributes.Price,
			Address:      address,
			UrlPath:      agencyLead.Attributes.Link,
			ImagePath:    imagePath,
			IsAgencyItem: false,
			Deeplink:     &agencyLead.Attributes.Deeplink,
		}
	}

	return itemInfos, nil
}
