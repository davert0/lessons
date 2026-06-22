package main

import (
	"constraints"
	//"fmt"
	"os"
	"strconv"
)

type Pair[T constraints.Ordered] struct {
	First  T
	Second T
}

// Порядковый номер - 10
// Номер задачи - 4
// Краткое название - декартово произведение множеств
// Сложность временная и пространственная (M*N)
// Рефлексия - если лениво итерироваться через генератор пространственную сложность можно снизить до O(1)
func (s *PowerSet[T]) CartesianProductSlice(set2 PowerSet[T]) []Pair[T] {
	var result []Pair[T]
	for elem1 := range s.dict {
		for elem2 := range set2.dict {
			result = append(result, Pair[T]{First: elem1, Second: elem2})
		}
	}
	return result
}

// Порядковый номер - 10
// Номер задачи - 5
// Краткое название - пересечение N множеств
// Сложность временная O(N * n)
// Сложность пространственная O(N)
// Рефлексия - итерируемся по наименьшему для экономии 
func IntersectionOfMany[T constraints.Ordered](sets ...*PowerSet[T]) PowerSet[T] {
	if len(sets) < 3 {
		panic("IntersectionOfMany requires at least 3 sets")
	}

	smallest := 0
	for i := 1; i < len(sets); i++ {
		if sets[i].Size() < sets[smallest].Size() {
			smallest = i
		}
	}

	result := Init[T]()

	for elem := range sets[smallest].dict {
		inAll := true
		for i := range sets {
			if i == smallest {
				continue
			}
			if !sets[i].Get(elem) {
				inAll = false
				break
			}
		}
		if inAll {
			result.Put(elem)
		}
	}

	return result
}

// Порядковый номер - 10
// Номер задачи - 6
// Краткое название - мультимножество
// Рефлексия - сначала звучало как оксюморон, но потом понял, что речь идет о счетчике
type Bag[T constraints.Ordered] struct {
	elements map[T]int
}

func NewBag[T constraints.Ordered]() *Bag[T] {
	return &Bag[T]{
		elements: make(map[T]int),
	}
}

// Добавление элемента в мультимножество
func (b *Bag[T]) Add(value T, count int) {
	if count <= 0 {
		return
	}
	b.elements[value] += count
}

// Удаление одного экземпляра элемента
func (b *Bag[T]) RemoveOne(value T) bool {
	if count, exists := b.elements[value]; exists {
		if count > 1 {
			b.elements[value]--
		} else {
			delete(b.elements, value)
		}
		return true
	}
	return false
}

// Получение списка всех элементов с их частотами
func (b *Bag[T]) GetElementsWithFrequencies() map[T]int {
	result := make(map[T]int)
	for elem, count := range b.elements {
		result[elem] = count
	}
	return result
}

// Получение количества вхождений элемента
func (b *Bag[T]) GetCount(value T) int {
	return b.elements[value]
}

// Удаление всех экземпляров элемента
func (b *Bag[T]) RemoveAll(value T) bool {
	if _, exists := b.elements[value]; exists {
		delete(b.elements, value)
		return true
	}
	return false
}

// Размер мультимножества (общее количество элементов с учётом кратности)
func (b *Bag[T]) TotalSize() int {
	total := 0
	for _, count := range b.elements {
		total += count
	}
	return total
}

// Уникальный размер (количество уникальных элементов)
func (b *Bag[T]) UniqueSize() int {
	return len(b.elements)
}
