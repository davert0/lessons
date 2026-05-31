package main

import (
	"cmp"
	"errors"
	"fmt"
	"maps"
)

// Порядковый номер - 7
// Номер задачи - 8
// Краткое название - удаление дубликатов
// Сложность O(N) временная, O(1) пространственная
// Рефлексия - ну тут все достаточно просто, так как список отсортирован и дубликаты идут подряд
func (l *OrderedList[T]) RemoveDuplicates() {
	if l.head == nil {
		return
	}

	current := l.head
	for current != nil && current.next != nil {
		if l.Compare(current.value, current.next.value) == 0 {
			nodeToRemove := current.next
			current.next = nodeToRemove.next
			if nodeToRemove.next != nil {
				nodeToRemove.next.prev = current
			} else {
				l.tail = current
			}
		} else {
			current = current.next
		}
	}
}

// Порядковый номер - 7
// Номер задачи - 9
// Краткое название - слияние упорядоченных списков
// Сложность O(N+M) временная, O(1) пространственная
// Рефлексия - также похоже на merge двух обычных linked-list'ов
func (l *OrderedList[T]) Merge(other *OrderedList[T]) error {
	if l._ascending != other._ascending {
		return errors.New("списки должны иметь одинаковый порядок сортировки")
	}

	if other.head == nil {
		return nil
	}

	if l.head == nil {
		l.head = other.head
		l.tail = other.tail
		return nil
	}

	a := l.head
	b := other.head
	var head, tail *Node[T]

	attach := func(n *Node[T]) {
		n.prev = tail
		if tail == nil {
			head = n
		} else {
			tail.next = n
		}
		tail = n
	}

	for a != nil && b != nil {
		if (l._ascending && l.Compare(a.value, b.value) <= 0) ||
			(!l._ascending && l.Compare(a.value, b.value) >= 0) {
			next := a.next
			attach(a)
			a = next
		} else {
			next := b.next
			attach(b)
			b = next
		}
	}

	rest, restTail := a, l.tail
	if a == nil {
		rest, restTail = b, other.tail
	}
	if rest != nil {
		rest.prev = tail
		tail.next = rest
		tail = restTail
	}
	tail.next = nil

	l.head = head
	l.tail = tail

	return nil
}

// Порядковый номер - 7
// Номер задачи - 10
// Краткое название - наличие подсписка в списке
// Сложность O(N*M) временная, O(1) пространственная.
// Рефлексия - в целом достаточно понятно, можно было бы решить через рекурсию
func (l *OrderedList[T]) Contains(sublist []T) bool {
	if len(sublist) == 0 {
		return true
	}

	current := l.head
	for current != nil {
		cmp := l.Compare(current.value, sublist[0])
		if (l._ascending && cmp > 0) || (!l._ascending && cmp < 0) {
			return false
		}
		if cmp == 0 && l.checkSublistFromNode(current, sublist) {
			return true
		}
		current = current.next
	}
	return false
}

func (l *OrderedList[T]) checkSublistFromNode(startNode *Node[T], sublist []T) bool {
	current := startNode
	for i := 0; i < len(sublist); i++ {
		if current == nil || l.Compare(current.value, sublist[i]) != 0 {
			return false
		}
		current = current.next
	}
	return true
}

// Порядковый номер - 7
// Номер задачи - 11
// Краткое название - самый частотный элемент
// Сложность O(N) временная, O(1) пространственная.
// Рефлексия - за счет упорядоченности можно обойтись без дополнительной памяти
func (l *OrderedList[T]) FindMostFrequent() (T, int, error) {
	var zeroValue T
	if l.head == nil {
		return zeroValue, 0, errors.New("список пуст")
	}

	maxCount := 0
	maxValue := zeroValue
	currentCount := 1
	currentValue := l.head.value

	current := l.head.next
	for current != nil {
		if l.Compare(current.value, currentValue) == 0 {
			currentCount++
		} else {
			if currentCount > maxCount {
				maxCount = currentCount
				maxValue = currentValue
			}
			currentValue = current.value
			currentCount = 1
		}
		current = current.next
	}

	if currentCount > maxCount {
		maxCount = currentCount
		maxValue = currentValue
	}

	return maxValue, maxCount, nil
}

type IndexedOrderedList[T cmp.Ordered] struct {
	OrderedList[T]
	nodes []*Node[T]
}

func (l *IndexedOrderedList[T]) Add(item T) {
	l.OrderedList.Add(item)
	l.rebuildIndex()
}

func (l *IndexedOrderedList[T]) Delete(item T) {
	l.OrderedList.Delete(item)
	l.rebuildIndex()
}

func (l *IndexedOrderedList[T]) Clear(asc bool) {
	l.OrderedList.Clear(asc)
	l.nodes = nil
}

func (l *IndexedOrderedList[T]) rebuildIndex() {
	count := l.Count()
	l.nodes = make([]*Node[T], 0, count)
	current := l.head
	for current != nil {
		l.nodes = append(l.nodes, current)
		current = current.next
	}
}

// Порядковый номер - 7
// Номер задачи - 12
// Краткое название - поиск индекса
// Сложность O(logN) временная на поиск,  O(1) пространственная
// Рефлексия - реализация сменена на слайс, используется бинарный поиск, также можно сделать на skip списке
func (l *IndexedOrderedList[T]) FindIndex(item T) (int, error) {
	count := l.Count()
	if count == 0 {
		return -1, errors.New("список пуст")
	}

	left, right := 0, count-1

	for left <= right {
		mid := (left + right) / 2
		cmp := l.Compare(l.nodes[mid].value, item)

		if cmp == 0 {
			for mid > 0 && l.Compare(l.nodes[mid-1].value, item) == 0 {
				mid--
			}
			return mid, nil
		} else if (l._ascending && cmp < 0) || (!l._ascending && cmp > 0) {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1, errors.New("элемент не найден")
}

func (l *IndexedOrderedList[T]) GetByIndex(index int) (T, error) {
	var zeroValue T
	count := l.Count()
	if index < 0 || index >= count {
		return zeroValue, errors.New("индекс вне диапазона")
	}
	return l.nodes[index].value, nil
}

func (l *OrderedList[T]) ToSlice() []T {
	count := l.Count()
	result := make([]T, 0, count)
	current := l.head
	for current != nil {
		result = append(result, current.value)
		current = current.next
	}
	return result
}

func (l *OrderedList[T]) Print() {
	fmt.Print("Список: ")
	current := l.head
	for current != nil {
		fmt.Printf("%v ", current.value)
		current = current.next
	}
	fmt.Printf("(порядок: %t, количество: %d)\n", l._ascending, l.Count())
}

func NewOrderedList[T cmp.Ordered](ascending bool) *OrderedList[T] {
	list := &OrderedList[T]{}
	list.Clear(ascending)
	return list
}

func NewIndexedOrderedList[T cmp.Ordered](ascending bool) *IndexedOrderedList[T] {
	list := &IndexedOrderedList[T]{}
	list.Clear(ascending)
	return list
}
