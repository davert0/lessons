package powerset

type PowerSet[T any] interface {
	HashTable[T]

	// запросы
	Intersection(set2 PowerSet[T]) PowerSet[T]
	Union(set2 PowerSet[T]) PowerSet[T]
	Difference(set2 PowerSet[T]) PowerSet[T]
	IsSubset(set2 PowerSet[T]) bool
	GetSlots() []T
}

type PowerSetImpl[T any] struct {
	HashTableImpl[T]
}

func NewPowerSetImpl[T any](maxSize int) PowerSet[T] {
	return &PowerSetImpl[T]{
		HashTableImpl[T]{
			maxSize: maxSize,
			step:    1,
			slots:   make([]T, maxSize),
		},
	}
}

func (p *PowerSetImpl[T]) Intersection(set2 PowerSet[T]) PowerSet[T] {

	intersectedSet := NewPowerSetImpl[T](p.Size())
	for _, el := range p.GetSlots() {
		if set2.FindValue(el) {
			intersectedSet.PutValue(el)
		}
	}
	return intersectedSet
}

func (p *PowerSetImpl[T]) Union(set2 PowerSet[T]) PowerSet[T] {
	unionSet := NewPowerSetImpl[T](p.Size() + set2.Size())

	for _, l := range append(p.GetSlots(), set2.GetSlots()...) {
		if l == nil {
			continue
		}
		unionSet.PutValue(l)
	}

	return unionSet
}

func (p *PowerSetImpl[T]) Difference(set2 PowerSet[T]) PowerSet[T] {
	diff := NewPowerSetImpl[T](p.size)

	for _, l := range p.GetSlots() {
		if set2.FindValue(l) {
			continue
		}

		diff.PutValue(l)
	}

	return diff
}

func (p *PowerSetImpl[T]) IsSubset(set2 PowerSet[T]) bool {
	for _, l := range set2.GetSlots() {
		if l == nil {
			continue
		}

		if !p.FindValue(l) {
			return false
		}
	}

	return true
}

func (p *PowerSetImpl[T]) GetSlots() []T {
	return p.slots
}
