package main

import (
	"errors"
	"fmt"
)

const bankerCreditsPerInsert = 2

// Порядковый номер - 3
// Номер задачи - 6
// Краткое название - банковский динамический массива
// Сложность O(1) амортизированная
// Рефлексия - не очень очевидное задание, но по итогу концепция интересная - накапливать кредиты на вставках и тратить на расширение и реаллокацию

type BankArray[T any] struct {
	count    int
	capacity int
	credits  int
	array    []T
}

func NewBankArray[T any]() BankArray[T] {
	ba := BankArray[T]{}
	ba.Init()

	return ba
}

func (da *BankArray[T]) Init() {
	da.count = 0
	da.credits = 0
	da.capacity = 1
	da.array = make([]T, 1)
}

func nextPowerOfTwo(n int) int {
	p := 1
	for p < n {
		p <<= 1
	}
	return p
}

func reallocPrice(count int) int {
	return nextPowerOfTwo(count + 1)
}

func (da *BankArray[T]) grow() {
	price := reallocPrice(da.count)
	newCap := da.capacity * 2
	newArr := make([]T, newCap)
	copy(newArr, da.array)
	da.credits -= price
	da.capacity = newCap
	da.array = newArr
}

func (da *BankArray[T]) Append(itm T) {
	da.credits += bankerCreditsPerInsert
	if da.credits >= reallocPrice(da.count) {
		da.grow()
	}
	da.array[da.count] = itm
	da.count++
}

func (da *BankArray[T]) Insert(itm T, index int) error {
	if index > da.count || index < 0 {
		return fmt.Errorf("bad index '%d'", index)
	}

	da.credits += bankerCreditsPerInsert
	if da.credits >= reallocPrice(da.count) {
		da.grow()
	}

	for i := da.count; i > index; i-- {
		da.array[i] = da.array[i-1]
	}
	da.array[index] = itm
	da.count++
	return nil
}

func (da *BankArray[T]) GetItem(index int) (T, error) {
	var zero T
	if index >= da.count || index < 0 {
		return zero, fmt.Errorf("index is out of range")
	}
	return da.array[index], nil
}

func (da *BankArray[T]) shrink() {
	price := reallocPrice(da.count)
	newCap := da.capacity / 2
	newArr := make([]T, newCap)
	copy(newArr, da.array[:da.count])
	da.credits -= price
	da.capacity = newCap
	da.array = newArr
}

func (da *BankArray[T]) Remove(index int) error {
	if index >= da.count || index < 0 {
		return fmt.Errorf("bad index '%d'", index)
	}

	for i := index; i < da.count-1; i++ {
		da.array[i] = da.array[i+1]
	}
	var zero T
	da.array[da.count-1] = zero
	da.count--

	da.credits += bankerCreditsPerInsert

	if da.capacity > 1 && 4*da.count <= da.capacity && da.credits >= reallocPrice(da.count) {
		da.shrink()
	}

	return nil
}



// Порядковый номер - 3
// Номер задачи - 7
// Краткое название - мульти-динамический-массив
// Рефлексия - тут вообще себе голову сломал, прежде чем пришел к плоской структуре со смещение по измерениям, изначально думал про вложенные массивы,
// но в go для этого нужно хранить что-то вроде DynArray[any] и кастить все вложенные структуры, получается так себе.

type MultiArray[T any] struct {
	dimensions int
	shape      []int
	data       []T
}

func NewMultiArray[T any](dimensions int, shape ...int) (*MultiArray[T], error) {
	if dimensions != len(shape) {
		return nil, errors.New("dimensions count doesn't match shape length")
	}

	totalSize := 1
	for _, size := range shape {
		if size <= 0 {
			return nil, errors.New("dimension size must be positive")
		}
		totalSize *= size
	}

	return &MultiArray[T]{
		dimensions: dimensions,
		shape:      shape,
		data:       make([]T, totalSize),
	}, nil
}

func (ma *MultiArray[T]) Get(indices ...int) (T, error) {
	var zero T
	if len(indices) != ma.dimensions {
		return zero, errors.New("wrong number of indices")
	}

	index := 0
	stride := 1
	for i := ma.dimensions - 1; i >= 0; i-- {
		if indices[i] < 0 || indices[i] >= ma.shape[i] {
			return zero, fmt.Errorf("index %d out of range for dimension %d", indices[i], i)
		}
		index += indices[i] * stride
		stride *= ma.shape[i]
	}

	return ma.data[index], nil
}

func (ma *MultiArray[T]) Set(value T, indices ...int) error {
	if len(indices) != ma.dimensions {
		return errors.New("wrong number of indices")
	}

	index := 0
	stride := 1
	for i := ma.dimensions - 1; i >= 0; i-- {
		if indices[i] < 0 || indices[i] >= ma.shape[i] {
			return fmt.Errorf("index %d out of range for dimension %d", indices[i], i)
		}
		index += indices[i] * stride
		stride *= ma.shape[i]
	}

	ma.data[index] = value
	return nil
}

func (ma *MultiArray[T]) Resize(newShape ...int) error {
	if len(newShape) != ma.dimensions {
		return errors.New("wrong number of dimensions")
	}

	newTotalSize := 1
	for _, size := range newShape {
		if size <= 0 {
			return errors.New("dimension size must be positive")
		}
		newTotalSize *= size
	}

	newData := make([]T, newTotalSize)

	oldIndices := make([]int, ma.dimensions)
	for i := 0; i < len(ma.data); i++ {
		copyIndices := true
		for j := 0; j < ma.dimensions; j++ {
			if oldIndices[j] >= newShape[j] {
				copyIndices = false
				break
			}
		}

		if copyIndices {
			newIndex := 0
			stride := 1
			for k := ma.dimensions - 1; k >= 0; k-- {
				newIndex += oldIndices[k] * stride
				stride *= newShape[k]
			}
			newData[newIndex] = ma.data[i]
		}

		for j := ma.dimensions - 1; j >= 0; j-- {
			oldIndices[j]++
			if oldIndices[j] < ma.shape[j] {
				break
			}
			oldIndices[j] = 0
		}
	}

	ma.data = newData
	ma.shape = newShape
	return nil
}
