package example2

import (
	"context"
	"fmt"
)

type Usecase struct {
	auth                auth.Service
	agencyLeadRepo      agencyleads.Repository
	personalDataService personaldata.Service
	calltracking        calltracking.Gateway
	logger              internal.Log
}

func NewUsecase(
	auth auth.Service,
	agencyLeadRepo agencyleads.Repository,
	personalDataService personaldata.Service,
	calltracking calltracking.Gateway,
	logger internal.Log,
) *Usecase {
	return &Usecase{
		auth:                auth,
		agencyLeadRepo:      agencyLeadRepo,
		calltracking:        calltracking,
		logger:              logger,
		personalDataService: personalDataService,
	}
}

func (s *Usecase) GetLeadContacts(ctx context.Context, dealID internal.AgencyLeadID) (*contracts.GetContactsData, error) {
	deal, err := s.agencyLeadRepo.GetAgencyLead(ctx, dealID)
	if err != nil {
		return nil, fmt.Errorf("err get agency lead data, %w", err)
	}

	if err = s.getLeadContactsPredicate(ctx, deal); err != nil {
		return nil, err
	}

	var (
		phoneNumber string
		isVirtual   bool
	)

	phoneNumber, err = s.getPhone(ctx, *deal)
	if err != nil {
		return nil, fmt.Errorf("decrypt seller phone: %w", err)
	}

	if s.isAgentsFirstContact(*deal) {
		virtualPhone, err := s.getVirtualPhone(ctx, *deal, phoneNumber)
		if err != nil {
			ctx = s.logger.WithFields(ctx, map[string]interface{}{
				"deal":   deal.ID,
				"method": "get_phone_for_agent",
			})
			s.logger.Warning(ctx, "error while virtual number generating, return real phone as fallback")
		}
		phoneNumber = virtualPhone
		isVirtual = true
	}

	return &contracts.GetContactsData{
		Phone: phoneNumber,
		Properties: contracts.PhoneProperties{
			IsVirtual:           isVirtual,
			QuestionnairePassed: deal.ContactQuestionnairePassed,
			RealCallCompleted:   deal.ContactedWithSeller,
		},
	}, nil

}

func (s *Usecase) isAgentsFirstContact(deal model.AgencyLead) bool {
	return !(deal.ContactQuestionnairePassed && deal.ContactedWithSeller)
}

func (s *Usecase) getLeadContactsPredicate(ctx context.Context, agencyLead *model.AgencyLead) error {
	userID := *agencyLead.Seller.UserID

	if agencyLead == nil {
		return contracts.ErrAgencyLeadNotFound
	}

	ok, err := s.auth.IsUserAccessAllowedToAgency(ctx, userID, agencyLead.AgencyID)
	if err != nil {
		return fmt.Errorf("check user authorization by agency id: %w", err)
	}
	if !ok {
		return contracts.ErrAgencyPermission
	}
	return nil
}

func (s *Usecase) getVirtualPhone(ctx context.Context, agencyLead model.AgencyLead, phone string) (string, error) {

	if agencyLead.VirtualPhoneID != nil {
		info, err := s.calltracking.GetVirtualNumberInfo(ctx, *agencyLead.VirtualPhoneID)
		if err != nil {
			return "", fmt.Errorf("get virtual number info: %w", err)
		}
		if !info.IsActive {
			return "", fmt.Errorf("virtual phone is not active")
		}
		return info.Phone, nil
	}

	if agencyLead.Attributes.Location == nil {
		return "", fmt.Errorf("agency lead location is absent but required for virtual number generating, return real phone as fallback")
	}

	virtualPhone, err := s.calltracking.GetVirtualNumber(ctx, phone, *agencyLead.Attributes.Location)
	if err != nil {
		return "", fmt.Errorf("get virtual number: %w", err)
	}

	err = s.agencyLeadRepo.UpdateAgencyLeadVirtualPhoneID(ctx, agencyLead.ID, virtualPhone.ID)
	if err != nil {
		return "", fmt.Errorf("update agency lead virtual phone id: %w", err)
	}

	return virtualPhone.Number, nil
}

func (s *Usecase) getPhone(ctx context.Context, agencyLead model.AgencyLead) (string, error) {
	phone, err := s.personalDataService.GetSellerPhone(ctx, agencyLead.Seller)
	if err != nil {
		return "", fmt.Errorf("decrypt seller phone: %w", err)
	}

	return phone, nil
}
