package second

import (
	"context"
	"fmt"
)

func (s *DefaultService) GetAgencyCPABalances(ctx context.Context, agencyIDs []internal.AgencyID) (map[internal.AgencyID]model.PennyBalance, error) {
	agencies, err := s.agencies.GetAgenciesByIDs(ctx, agencyIDs)
	if err != nil {
		return nil, fmt.Errorf("get agencies by ids: %w", err)
	}

	agenciesIDsWithNewBilling := make([]model.Agency, 0, len(agencyIDs))
	for _, agency := range agencies {
		if !agency.HasCPABillingEnabled {
			continue
		}

		agenciesIDsWithNewBilling = append(agenciesIDsWithNewBilling, agency)
	}

	result := make(map[internal.AgencyID]model.PennyBalance, len(agencyIDs))
	if len(agenciesIDsWithNewBilling) > 0 {
		for _, agency := range agenciesIDsWithNewBilling {
			balance, err := s.cpa.GetBalance(ctx, agency.RootUserID)

			if err != nil {
				return nil, err
			}

			result[agency.ID] = model.PennyBalance(balance)
		}
	}

	return result, err
}
