package main

import (
	"errors"
	// "fmt"
	"sort"
)

// Порядковый номер - 9
// Номер задачи - 5
// Краткое название - отсортированный словарь
// Временная сложность - O(logN) поиск, O(N) вставка и удаление (за счет смещения)
// Рефлексия - интересно, даже не задумывался, что в словаре можно обходится без хэш таблицы и сохранять высокую скорость поиска
type OrderedDictionary[T any] struct {
	keys   []string
	values []T
}

func InitOrderedDict[T any]() OrderedDictionary[T] {
	return OrderedDictionary[T]{
		keys:   make([]string, 0),
		values: make([]T, 0),
	}
}

func (od *OrderedDictionary[T]) findKey(key string) (int, bool) {
	i := sort.SearchStrings(od.keys, key)
	if i < len(od.keys) && od.keys[i] == key {
		return i, true
	}
	return i, false
}

func (od *OrderedDictionary[T]) Put(key string, value T) {
	idx, found := od.findKey(key)
	if found {
		od.values[idx] = value
	} else {
		od.keys = append(od.keys, "")
		od.values = append(od.values, value)
		copy(od.keys[idx+1:], od.keys[idx:])
		copy(od.values[idx+1:], od.values[idx:])

		od.keys[idx] = key
		od.values[idx] = value
	}
}

func (od *OrderedDictionary[T]) Get(key string) (T, error) {
	var result T
	idx, found := od.findKey(key)
	if !found {
		return result, errors.New("ключ не найден")
	}
	return od.values[idx], nil
}

func (od *OrderedDictionary[T]) Remove(key string) error {
	idx, found := od.findKey(key)
	if !found {
		return errors.New("ключ не найден")
	}
	od.keys = append(od.keys[:idx], od.keys[idx+1:]...)
	od.values = append(od.values[:idx], od.values[idx+1:]...)
	return nil
}

func (od *OrderedDictionary[T]) IsKey(key string) bool {
	_, found := od.findKey(key)
	return found
}

// Порядковый номер - 9
// Номер задачи - 6
// Краткое название - Словарь с битовыми ключами фиксированной длины
// - Сложность операций:
//  - Put: O(1) (bitSize)
//  - Get: O(1) (bitSize)
// Рефлексия - самое сложнео конечно было понять что от меня вообще хотят, а потом вспомнить что битовые операции это не страшно

const bitSize = 32

type node[T any] struct {
	children [2]*node[T]
	hasValue bool
	value    T
}

type BitTrie[T any] struct{ root *node[T] }

func InitBitTrie[T any]() BitTrie[T] {
	return BitTrie[T]{root: &node[T]{}}
}

func (t *BitTrie[T]) Put(key uint32, value T) {
	n := t.root
	for i := bitSize - 1; i >= 0; i-- {
		bit := (key >> uint(i)) & 1
		if n.children[bit] == nil {
			n.children[bit] = &node[T]{}
		}
		n = n.children[bit]
	}
	n.hasValue, n.value = true, value
}

func (t *BitTrie[T]) Get(key uint32) (T, bool) {
	n := t.root
	for i := bitSize - 1; i >= 0; i-- {
		bit := (key >> uint(i)) & 1
		if n.children[bit] == nil {
			var zero T
			return zero, false
		}
		n = n.children[bit]
	}
	return n.value, n.hasValue
}
