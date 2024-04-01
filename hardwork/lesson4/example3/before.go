package example3

import (
	"context"
	"fmt"
)

type Service interface {
	GetList(
		ctx context.Context,
		agencyID internal.AgencyID,
		spec contracts.AgencyLeadListSpecification,
	) ([]contracts.AgencyLeadListItemData, error)
}

type Usecase struct {
	agencyRepo         agencies.Repository
	agencyLeadsService Service
}

func NewUsecase(
	agencyRepo agencies.Repository,
	agencyLeadsService agencyleadslist.Service,
) *Usecase {
	return &Usecase{
		agencyRepo:         agencyRepo,
		agencyLeadsService: agencyLeadsService,
	}
}

func (s *Usecase) GetAgencyLeadsListByUserIDAndSpec(ctx context.Context, userID external.UserID, spec contracts.AgencyLeadListSpecification) ([]contracts.AgencyLeadListItemData, error) {
	agency, err := s.agencyRepo.GetAgencyByUserID(ctx, userID)
	if err != nil {
		return nil, fmt.Errorf("get agency by user id: %w", err)
	}
	if agency == nil {
		return nil, contracts.ClientError{
			Message: "agency access denied by user",
			Details: map[string]any{"userID": userID},
		}
	}

	return s.agencyLeadsService.GetList(ctx, agency.ID, spec)
}
