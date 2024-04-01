package example3


type (
	Usecase struct {
		deals     deals.Repository
		converter Converter
	}
)

func New(deals deals.Repository, converter Converter) *Usecase {
	return &Usecase{deals: deals, converter: converter}
}

func (u *Usecase) Handle(
	ctx security.Context,
	in *contracts.GetDealsIn,
	request pageable.Request[dicts.SortGetDeals],
) (pageable.Page[contracts.Deal], error) {
	spec := &deals.GetAllDealsSpecification{
		MemberIn: in.MemberIn,
		StatusIn: in.StatusIn,
	}

	if err := policy.GetDealsPredicate(ctx, spec); err != nil {
		return nil, err
	}

	page, err := u.deals.GetAllDeals(ctx, spec, request)
	if err != nil {
		return nil, err
	}

	return pageable.SafeMap(page, u.converter.Convert), nil