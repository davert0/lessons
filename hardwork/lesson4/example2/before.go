package example2

import (
	"context"
	"errors"
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

func (s *Usecase) GetLeadContacts(ctx context.Context, leadID internal.AgencyLeadID, userID external.UserID) (*contracts.GetContactsData, error) {
	agencyLead, err := s.agencyLeadRepo.GetAgencyLead(ctx, leadID)
	if err != nil {
		return nil, fmt.Errorf("err get agency lead data, %w", err)
	}
	if agencyLead == nil {
		return nil, contracts.ErrAgencyLeadNotFound
	}

	ok, err := s.auth.IsUserAccessAllowedToAgency(ctx, userID, agencyLead.AgencyID)
	if err != nil {
		return nil, fmt.Errorf("check user authorization by agency id: %w", err)
	}
	if !ok {
		return nil, contracts.ErrAgencyPermission
	}

	var (
		sellerPhone string
		isVirtual   bool
		sellerName  string
	)

	eg, ctx := errgroup.WithContext(ctx)
	eg.Go(func() error {
		var err error
		sellerPhone, isVirtual, err = s.getPhoneForAgent(ctx, *agencyLead)
		if err != nil {
			return fmt.Errorf("get seller phone: %w", err)
		}
		return nil
	})
	eg.Go(func() error {
		var err error
		sellerName, err = s.getName(ctx, *agencyLead)
		if err != nil {
			return fmt.Errorf("get seller name: %w", err)
		}
		return nil
	})

	err = eg.Wait()
	if err != nil {
		return nil, err
	}

	return &contracts.GetContactsData{
		Phone: sellerPhone,
		Name:  sellerName,
		Properties: contracts.PhoneProperties{
			IsVirtual:           isVirtual,
			QuestionnairePassed: agencyLead.ContactQuestionnairePassed,
			RealCallCompleted:   agencyLead.ContactedWithSeller,
		},
	}, nil
}

func (s *Usecase) getPhoneForAgent(ctx context.Context, agencyLead model.AgencyLead) (string, bool, error) {
	phoneNumber, err := s.getPhone(ctx, agencyLead)
	if err != nil {
		return "", false, fmt.Errorf("decrypt seller phone: %w", err)
	}

	if agencyLead.ContactQuestionnairePassed && agencyLead.ContactedWithSeller {
		return phoneNumber, false, nil
	}

	if agencyLead.VirtualPhoneID != nil {
		info, err := s.calltracking.GetVirtualNumberInfo(ctx, *agencyLead.VirtualPhoneID)
		switch {
		case err != nil:
			return "", false, fmt.Errorf("get virtual number info: %w", err)
		case info.IsActive:
			return info.Phone, true, nil
		default:
			return phoneNumber, false, nil
		}
	}

	if agencyLead.Attributes.Location == nil {
		ctx = s.logger.WithFields(ctx, map[string]interface{}{
			"agency_lead_id": agencyLead.ID,
			"method":         "get_phone_for_agent",
		})
		s.logger.Warning(ctx, "agency lead location is absent but required for virtual number generating, return real phone as fallback")

		return phoneNumber, false, nil
	}

	virtualPhone, err := s.calltracking.GetVirtualNumber(ctx, phoneNumber, *agencyLead.Attributes.Location)
	if errors.Is(err, calltracking.ErrPhonePoolEmpty) {
		return phoneNumber, false, nil
	}
	if err != nil {
		return "", false, fmt.Errorf("get virtual number: %w", err)
	}

	err = s.agencyLeadRepo.UpdateAgencyLeadVirtualPhoneID(ctx, agencyLead.ID, virtualPhone.ID)
	if err != nil {
		return "", false, fmt.Errorf("update agency lead virtual phone id: %w", err)
	}

	return virtualPhone.Number, true, nil
}

func (s *Usecase) getName(ctx context.Context, agencyLead model.AgencyLead) (string, error) {
	name, err := s.personalDataService.GetSellerName(ctx, agencyLead.Seller)
	if err != nil {
		return "", fmt.Errorf("decrypt seller name: %w", err)
	}

	return name, nil
}

func (s *Usecase) getPhone(ctx context.Context, agencyLead model.AgencyLead) (string, error) {
	name, err := s.personalDataService.GetSellerPhone(ctx, agencyLead.Seller)
	if err != nil {
		return "", fmt.Errorf("decrypt seller phone: %w", err)
	}

	return name, nil
}
