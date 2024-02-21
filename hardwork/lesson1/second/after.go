package second

import (
	"context"
	"fmt"
)

func (s *DefaultService) GetAgencyCPABalances2(ctx context.Context, agencyIDs []internal.AgencyID) (map[internal.AgencyID]model.PennyBalance, error) {
	agencies, err := s.agencies.GetAgenciesByIDs(ctx, agencyIDs)
	if err != nil {
		return nil, fmt.Errorf("get agencies by ids: %w", err)
	}

	agenciesWithNewBilling := slices.Filter(agencies, func(agency model.Agency) bool {
		return agency.HasCPABillingEnabled
	})

	result := make(map[internal.AgencyID]model.PennyBalance, len(agencyIDs))
	for _, agency := range agenciesWithNewBilling {
		balance, err := s.cpa.GetBalance(ctx, agency.RootUserID)

		if err != nil {
			return nil, err
		}

		result[agency.ID] = model.PennyBalance(balance)
	}

	return result, err
}
