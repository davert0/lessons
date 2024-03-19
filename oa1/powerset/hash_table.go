package powerset

import "errors"

const (
	NotCalled Status = iota // Замените эти значения на соответствующие константы из вашего кода на C#
	FailSizeExceeded
	FailCantPut
	Ok
	FailNotFound
)

type Status int

type HashTable[T any] interface {
	// команды

	// предусловие - таблица не заполнена
	// постусловие - в таблицу добавлен элемент
	PutValue(value T)

	// запросы

	// предусловие - таблица не пуста
	FindValue(value T) bool

	Size() int
	GetPutStatus() Status
	GetFindStatus() Status
}

type HashTableImpl[T any] struct {
	size, maxSize, step             int
	findValueStatus, putValueStatus Status
	slots                           []T
}

func NewHashTableImpl[T any](maxSize int) *HashTableImpl[T] {
	return &HashTableImpl[T]{
		maxSize: maxSize,
		step:    1,
		slots:   make([]T, maxSize),
	}
}

func (h *HashTableImpl[T]) PutValue(value T) {
	if h.size == h.maxSize {
		h.putValueStatus = FailSizeExceeded
		return
	}

	idx, err := h.SeekSlot(value)
	if err != nil {
		h.putValueStatus = FailCantPut
		return
	}

	h.slots[idx] = value
	h.putValueStatus = Ok
}

func (h *HashTableImpl[T]) FindValue(value T) bool {
	_, err := h.SeekSlot(value)
	if err != nil {
		h.findValueStatus = FailNotFound
		return false
	}

	h.findValueStatus = Ok
	return true
}

func (h *HashTableImpl[T]) Size() int {
	return h.size
}

func (h *HashTableImpl[T]) GetFindStatus() Status {
	return h.findValueStatus
}

func (h *HashTableImpl[T]) GetPutStatus() Status {
	return h.putValueStatus
}

func (h *HashTableImpl[T]) FindIndex(value interface{}) int {
	hash := value.(int)
	return abs(hash % h.size)
}

func (h *HashTableImpl[T]) SeekSlot(value T) (int, error) {
	idx := h.FindIndex(value)
	if h.slots[idx] == nil {
		return idx, nil
	}

	for curIdx := idx + h.step; curIdx < h.size; curIdx += h.step {
		if h.slots[curIdx] == nil {
			return curIdx, nil
		}
	}
	for curIdx := 0; curIdx < idx; curIdx += h.step {
		if h.slots[curIdx] == nil {
			return curIdx, nil
		}
	}

	return -1, errors.New("unable to seek slot")
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
