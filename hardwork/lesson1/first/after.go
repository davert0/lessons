package first

import (
	"context"
	"errors"
	"fmt"
)

func (d *DefaultService) ExtractItemInfoFromAgencyLeads2(ctx context.Context, agencyLeads ...model.AgencyLead) (map[internal.AgencyLeadID]model.AgencyLeadItemInfo, error) {
	leadsWithItemID := slices.Filter(agencyLeads, func(lead model.AgencyLead) bool {
		return lead.ItemID != nil
	})
	leadsWithoutItemID := slices.Filter(agencyLeads, func(lead model.AgencyLead) bool {
		return lead.ItemID == nil
	})

	itemInfosFromLeadsWithItemID, err := d.getItemInfoFromLeadsWithItemID(ctx, leadsWithItemID)
	if err != nil {
		return nil, err
	}

	itemInfosFromLeadsWithoutItemID := d.getItemInfoFromLeadsWithoutItemID(ctx, leadsWithoutItemID)

	itemInfos := maps.Union(itemInfosFromLeadsWithItemID, itemInfosFromLeadsWithoutItemID)

	return itemInfos, nil
}

func (d *DefaultService) getItemInfoFromLeadsWithoutItemID(ctx context.Context, leadsWithoutItemID []model.AgencyLead) map[internal.AgencyLeadID]model.AgencyLeadItemInfo {
	itemInfos := make(map[internal.AgencyLeadID]model.AgencyLeadItemInfo, len(leadsWithoutItemID))
	for _, agencyLead := range leadsWithoutItemID {
		itemInfo := d.getItemInfoFromAgencyLeadAttrs(ctx, agencyLead)
		itemInfos[agencyLead.ID] = itemInfo
	}
	return itemInfos
}

func (d *DefaultService) getItemInfoFromLeadsWithItemID(ctx context.Context, leadsWithItemID []model.AgencyLead) (map[internal.AgencyLeadID]model.AgencyLeadItemInfo, error) {
	itemIDs, _ := slices.Map(leadsWithItemID, func(lead model.AgencyLead) (external.ItemID, error) {
		return *lead.ItemID, nil
	})
	items, err := d.fetchItems(ctx, itemIDs)
	if err != nil && !errors.Is(err, errEmptyItems) {
		return nil, fmt.Errorf("fetch items: %w", err)
	}
	itemInfos := make(map[internal.AgencyLeadID]model.AgencyLeadItemInfo, len(items))
	for _, agencyLead := range leadsWithItemID {
		item, _ := items[*agencyLead.ItemID]
		itemInfo := d.getItemInfoFromItemsService(ctx, item, agencyLead)
		itemInfos[agencyLead.ID] = itemInfo
	}
	return itemInfos, nil
}

func (d *DefaultService) getItemInfoFromAgencyLeadAttrs(ctx context.Context, agencyLead model.AgencyLead) model.AgencyLeadItemInfo {
	address := ""
	if agencyLead.Attributes.AddressString != nil {
		address = *agencyLead.Attributes.AddressString
	}

	imagePath := d.getImageUrlByID(ctx, agencyLead.ID, agencyLead.Attributes.ImageID)
	itemInfo := model.AgencyLeadItemInfo{
		Title:        agencyLead.Attributes.Title,
		Price:        agencyLead.Attributes.Price,
		Address:      address,
		UrlPath:      agencyLead.Attributes.Link,
		ImagePath:    imagePath,
		IsAgencyItem: false,
		Deeplink:     &agencyLead.Attributes.Deeplink,
	}
	return itemInfo
}

func (d *DefaultService) getItemInfoFromItemsService(
	ctx context.Context,
	item itemGateway.Item,
	agencyLead model.AgencyLead,
) model.AgencyLeadItemInfo {
	var address string
	if item.Address != nil {
		address = *item.Address
	}

	imagePath := d.getImageUrlByID(ctx, agencyLead.ID, item.ImageID)
	deeplink := d.makeDeeplink(ctx, item.ID)
	itemInfo := model.AgencyLeadItemInfo{
		Title:        item.Title,
		Price:        item.Price,
		Address:      address,
		UrlPath:      item.Link,
		ImagePath:    imagePath,
		IsAgencyItem: true,
		Deeplink:     deeplink,
	}
	return itemInfo
}
