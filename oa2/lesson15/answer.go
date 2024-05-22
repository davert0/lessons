package lesson15

// В зависимости от ликвидности лида, возвращается различный приоритет для планировщика
// Вместо условной цепочки используется полиморфизм

const (
	High LeadPriority = iota
	Mid
	Low
)

type LeadPriority int

type Lead interface {
	GetPriority() LeadPriority
}

type HighLiquidityLead struct{}

func (h HighLiquidityLead) GetPriority() LeadPriority {
	return High
}

type DefaultLead struct{}

func (d DefaultLead) GetPriority() LeadPriority {
	return Mid
}

type LowLiquidityLead struct{}

func (l LowLiquidityLead) GetPriority() LeadPriority {
	return Low
}
