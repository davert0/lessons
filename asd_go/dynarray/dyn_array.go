package main

import (
	"fmt"
	"os"
)

const (
	increaseRate = 2
	decreaseRate = 1.5
	minCap       = 0.5
)

type DynArray[T any] struct {
	count    int
	capacity int
	array    []T
}

func (da *DynArray[T]) Init() {
	da.count = 0
	da.MakeArray(16)
}

func (da *DynArray[T]) MakeArray(sz int) {
	if sz < 16 {
		sz = 16
	}

	arr := make([]T, sz)

	if da.count != 0 {
		copy(arr, da.array)
	}
	da.capacity = sz
	da.array = arr
}

// O(N)
func (da *DynArray[T]) Insert(itm T, index int) error {
	if index > da.count || index < 0 {
		return fmt.Errorf("bad index '%d'", index)
	}

	if da.count == da.capacity {
		da.MakeArray(da.capacity * increaseRate)
	}

	if index == da.count {
		da.array[index] = itm
		da.count++
		return nil
	}

	for i := da.count; i > index; i-- {
		da.array[i] = da.array[i-1]
	}

	da.array[index] = itm

	da.count++

	return nil
}

// O(N)
func (da *DynArray[T]) Remove(index int) error {
	if index >= da.count || index < 0 {
		return fmt.Errorf("bad index '%d'", index)
	}

	for i := index; i < da.count-1; i++ {
		da.array[i] = da.array[i+1]
	}

	da.count--

	decreasedCap := int(float64(da.capacity) * minCap)

	if da.count < decreasedCap {
		newSize := int(float64(da.capacity) / decreaseRate)

		da.MakeArray(newSize)
	}

	return nil
}

func (da *DynArray[T]) Append(itm T) {
	if da.count == da.capacity {
		da.MakeArray(da.capacity * increaseRate)
	}

	da.array[da.count] = itm
	da.count++
}

func (da *DynArray[T]) GetItem(index int) (T, error) {
	var result T
	if index >= da.count || index < 0 {
		return result, fmt.Errorf("index is out of range")
	}

	return da.array[index], nil
}
