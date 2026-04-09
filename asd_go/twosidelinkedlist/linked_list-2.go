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
// Рефлексия - пришлось вспоминать принцип обычной сортировки пузырьком
func (l *LinkedList2) Sort() {
	if l.head == nil {
		return
	}

	swapped := true
	for swapped {
		swapped = false
		node := l.head
		for node.next != nil {
			if node.value > node.next.value {
				node.value, node.next.value = node.next.value, node.value
				swapped = true
			}
			node = node.next
		}
	}
}

// Порядковый номер - 2
// Номер задачи - 12
// Краткое название - слияние двухсвязных списков
// Сложность O(N² + M²) - временная, O(N+M) - пространственная
// Рефлексия - сначала вручную прописывала все next и prev, потом вспомнил про наличие существующих методов AddInTail
func (l *LinkedList2) Merge(other *LinkedList2) *LinkedList2 {
	l.Sort()
	other.Sort()

	result := &LinkedList2{}
	a := l.head
	b := other.head

	for a != nil && b != nil {
		if a.value <= b.value {
			result.AddInTail(Node{value: a.value})
			a = a.next
		} else {
			result.AddInTail(Node{value: b.value})
			b = b.next
		}
	}

	for a != nil {
		result.AddInTail(Node{value: a.value})
		a = a.next
	}

	for b != nil {
		result.AddInTail(Node{value: b.value})
		b = b.next
	}

	return result
}
