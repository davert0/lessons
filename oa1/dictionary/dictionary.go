package dictionary

import (
	"math"
)

const (
	NotCalled Status = iota
	Ok
	FailNotFound
)

type Status int

type NativeDictionary[T any] interface {
	// команды

	// постусловие - элемент добавлен в словарь
	Put(key string, value T)

	// запросы

	//предусловие - элемент есть в словаре
	Get(key string) T
	HasKey(key string) bool
	GetStatus() Status
}

////запросы
//
////предусловие элемент найден
//public abstract T Get(string key);
//public abstract bool ContainsKey(string key);
//

type NativeDictionaryImpl[T any] struct {
	size   int
	slots  []string
	values []T
	status Status
}

func NewNativeDictionary[T any](size int) *NativeDictionaryImpl[T] {
	return &NativeDictionaryImpl[T]{
		size:   size,
		slots:  make([]string, size),
		values: make([]T, size),
		status: NotCalled,
	}
}

func (d *NativeDictionaryImpl[T]) Put(key string, value T) {
	idx := d.seekEmptySlot(key)
	d.slots[idx] = key
	d.values[idx] = value
}

func (d *NativeDictionaryImpl[T]) Get(key string) T {
	idx := d.seekSlot(key)
	if idx == -1 {
		d.status = FailNotFound
		return *new(T)
	}

	d.status = Ok
	return d.values[idx]
}

func (d *NativeDictionaryImpl[T]) HasKey(key string) bool {
	return d.seekSlot(key) >= 0
}

func (d *NativeDictionaryImpl[T]) GetStatus() Status {
	return d.status
}

func (d *NativeDictionaryImpl[T]) hashFun(key string) int {
	hash := int32(0)
	for _, c := range key {
		hash = 31*hash + int32(c)
	}

	res := int(math.Abs(float64(hash % int32(d.size))))
	return res
}

func (d *NativeDictionaryImpl[T]) seekSlot(value string) int {
	idx := d.hashFun(value)
	if d.slots[idx] == value {
		return idx
	}

	step := 1
	for curIdx := idx + step; curIdx < d.size; curIdx += step {
		if d.slots[curIdx] == value {
			return curIdx
		}
	}
	for curIdx := 0; curIdx < idx; curIdx += step {
		if d.slots[curIdx] == value {
			return curIdx
		}
	}
	return -1
}

func (d *NativeDictionaryImpl[T]) seekEmptySlot(value string) int {
	idx := d.hashFun(value)
	if d.slots[idx] == "" {
		return idx
	}

	step := 1
	for curIdx := idx + step; curIdx < d.size; curIdx += step {
		if d.slots[curIdx] == "" {
			return curIdx
		}
	}
	for curIdx := 0; curIdx < idx; curIdx += step {
		if d.slots[curIdx] == "" {
			return curIdx
		}
	}
	return idx
}
