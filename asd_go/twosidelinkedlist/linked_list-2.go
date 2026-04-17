package main

// Порядковый номер - 2
// Номер задачи - 9
// Краткое название - разворот двухсвязного списка
// Сложность O(N) - временная, O(1) - пространственная
// Рефлексия - самое приятное доп задание из списка, хорошо ложится в голову

func (l *LinkedList2) Reverse() {
	tail := l.tail
	head := l.head

	l.head = tail
	for tail != nil {
		buffer := tail.next
		tail.next = tail.prev
		tail.prev = buffer
		tail = tail.next
	}

	l.tail = head
}

// Порядковый номер - 2
// Номер задачи - 10
// Краткое название - проверка наличия цикла в двухсвязном списке
// Сложность O(N) - временная, O(1) - пространственная
// Рефлексия - один из моих любимых алгоритмов с быстрым и медленным указателем, 
func (l *LinkedList2) HasCycle() bool {
	slow := l.head
	fast := l.head

	for fast != nil && fast.next != nil {
		slow = slow.next
		fast = fast.next.next
		if slow == fast {
			return true
		}
	}

	return false
}

// Порядковый номер - 2
// Номер задачи - 11
// Краткое название - сортировка двухсвязного списка
// Сложность O(N^2) - временная, O(1) - пространственная
// Рефлексия - переписал с обмена значений на перецепление узлов, чтобы сохранить идентичность узлов для внешних ссылок
func (l *LinkedList2) Sort() {
	if l.head == nil {
		return
	}

	swapped := true
	for swapped {
		swapped = false
		node := l.head
		for node != nil && node.next != nil {
			if node.value > node.next.value {
				l.swapAdjacent(node, node.next)
				swapped = true
			} else {
				node = node.next
			}
		}
	}
}

func (l *LinkedList2) swapAdjacent(a, b *Node) {
	before := a.prev
	after := b.next

	if before != nil {
		before.next = b
	} else {
		l.head = b
	}
	if after != nil {
		after.prev = a
	} else {
		l.tail = a
	}

	b.prev = before
	b.next = a
	a.prev = b
	a.next = after
}

// Порядковый номер - 2
// Номер задачи - 12
// Краткое название - слияние двухсвязных списков
// Сложность O(N² + M²) - временная (доминирует сортировка), O(1) - пространственная
// Рефлексия - переписал с копирования значений на перенос существующих узлов через перецепление ссылок
func (l *LinkedList2) Merge(other *LinkedList2) *LinkedList2 {
	l.Sort()
	other.Sort()

	result := &LinkedList2{}
	a := l.head
	b := other.head

	for a != nil && b != nil {
		if a.value <= b.value {
			next := a.next
			result.attachNode(a)
			a = next
		} else {
			next := b.next
			result.attachNode(b)
			b = next
		}
	}

	for a != nil {
		next := a.next
		result.attachNode(a)
		a = next
	}

	for b != nil {
		next := b.next
		result.attachNode(b)
		b = next
	}

	l.head, l.tail = nil, nil
	other.head, other.tail = nil, nil

	return result
}

func (l *LinkedList2) attachNode(n *Node) {
	n.prev = l.tail
	n.next = nil
	if l.tail == nil {
		l.head = n
	} else {
		l.tail.next = n
	}
	l.tail = n
}
