package dynamicarray

import (
	"errors"
	"math"
)

const (
	InsertStatusNil InsertStatus = 0
	InsertStatusOk  InsertStatus = 1
	InsertStatusErr InsertStatus = 2
)

const (
	RemoveStatusNil RemoveStatus = 0
	RemoveStatusOk  RemoveStatus = 1
	RemoveStatusErr RemoveStatus = 2
)

const (
	GetItemStatusNil GetItemStatus = 0
	GetItemStatusOk  GetItemStatus = 1
	GetItemStatusErr GetItemStatus = 2
)

const MinArraySize = 16

type InsertStatus int
type RemoveStatus int
type GetItemStatus int

type DynArray[T any] interface {
	// команды

	// постусловие - добавлен новый элемент в конец массива.
	Append(item T)

	// предусловие - индекс не выходит за границы
	// постусловие -добавлен новый элемент по индексу
	Insert(item T, index int) error

	// предусловие - индекс не выходит за границы
	// постусловие - удален новый элемент по индексу
	Remove(index int) error

	// запросы

	Size() int

	// предусловие - индекс не выходит за границы
	GetItem(index int) (T, error)

	InsertStatus() InsertStatus
	RemoveStatus() RemoveStatus
	GetItemStatus() GetItemStatus
}

func NewDynArray[T any]() DynArray[T] {
	return &DynArrayImpl[T]{
		count:         0,
		insertStatus:  InsertStatusNil,
		removeStatus:  RemoveStatusNil,
		getItemStatus: GetItemStatusNil,
		capacity:      MinArraySize,
		arr:           make([]T, MinArraySize),
	}
}

type DynArrayImpl[T any] struct {
	arr           []T
	count         int
	capacity      int
	insertStatus  InsertStatus
	removeStatus  RemoveStatus
	getItemStatus GetItemStatus
}

func (da *DynArrayImpl[T]) Append(item T) {
	if da.count+1 > da.capacity {
		da.capacity = IncreasedCapacity(da.capacity)
		expandedArray := make([]T, da.capacity)
		copy(expandedArray, da.arr)
		da.arr = expandedArray
	}
	da.arr[da.count] = item
	da.count++
}

func (da *DynArrayImpl[T]) Insert(item T, index int) error {
	if index < 0 || index > da.count {
		da.insertStatus = InsertStatusErr
		return errors.New("index out of range")
	}

	if da.isFull() {
		da.makeArray(IncreasedCapacity(da.capacity))
	}

	if da.count > 0 {
		startToShiftIndex := index
		endToShiftIndex := index + 1
		shiftLength := da.count - index
		copy(da.arr[endToShiftIndex:], da.arr[startToShiftIndex:startToShiftIndex+shiftLength])
	}

	da.arr[index] = item

	da.count++

	da.insertStatus = InsertStatusOk
	return nil
}

func (da *DynArrayImpl[T]) Remove(index int) error {
	if index < 0 || index > da.count {
		da.removeStatus = RemoveStatusErr
		return errors.New("index out of range")
	}

	da.count--
	if da.count > 0 {
		da.arr = append(da.arr[:index], da.arr[index+1:]...)
	}
	fullness := da.getFullness()
	if fullness < 50 {
		da.makeArray(DecreasedCapacity(da.capacity))
	}
	da.removeStatus = RemoveStatusOk
	return nil
}

func (da *DynArrayImpl[T]) Size() int {
	return da.count
}

func (da *DynArrayImpl[T]) GetItem(index int) (T, error) {
	if index < 0 || index >= da.count {
		da.getItemStatus = GetItemStatusErr
		return *new(T), errors.New("index out of range")
	}
	da.getItemStatus = GetItemStatusOk
	return da.arr[index], nil
}

func (da *DynArrayImpl[T]) InsertStatus() InsertStatus {
	return da.insertStatus
}

func (da *DynArrayImpl[T]) RemoveStatus() RemoveStatus {
	return da.removeStatus
}

func (da *DynArrayImpl[T]) GetItemStatus() GetItemStatus {
	return da.getItemStatus
}

func (da *DynArrayImpl[T]) isFull() bool {
	return da.count == len(da.arr)
}

func (da *DynArrayImpl[T]) getFullness() float64 {
	if da.count == 0 {
		return 0
	}
	return float64(da.count/da.capacity) * 100
}

func (da *DynArrayImpl[T]) makeArray(capacity int) error {
	if capacity == da.capacity {
		return nil
	}

	if capacity <= 0 {
		errors.New("new capacity should be positive number")
	}
	newArr := make([]T, capacity)
	if da.count > 0 {
		copy(newArr, da.arr)
	}
	da.arr = newArr
	da.capacity = capacity
	return nil
}

func IncreasedCapacity(capacity int) int {
	if capacity == 0 {
		return MinArraySize
	}
	return int(math.Max(MinArraySize, float64(capacity*2)))
}

func DecreasedCapacity(capacity int) int {
	if capacity == 0 {
		return MinArraySize
	}
	return int(math.Max(MinArraySize, float64(capacity)/1.5))
}
