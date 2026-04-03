package main

import "errors"

// Порядковый номер - 1
// Номер задачи - 8
// Краткое название - сложение двух связных списков
// Сложность O(N) - временная и пространственная

func SumTwoLists(l1, l2 LinkedList) (LinkedList, error) {
	c1 := l1.Count()
	c2 := l2.Count()
	if c1 != c2 || c1 == 0 || c2 == 0 {
		return LinkedList{}, errors.New("invalid input")
	}

	res := LinkedList{}
	first := l1.head
	second := l2.head
	for first != nil && second != nil {
		newNode := Node{value: first.value + second.value}
		res.AddInTail(newNode)
		first = first.next
		second = second.next
	}
	return res, nil
}

// Рефлексия по заданию 8 - с удовольствием обновил реализацию связного списка, но больно было делать удаление - нужно держать в рабочей памяти сразу несколько узлов и их связей друг с другом.
// Для лучшей читаемости разделил delete на два метода, в зависимости от флага.
// Само задание sum two lists - база литкода, всегда полезно. Единственное, думал над сигнатурой, возвращать ошибку или нет, но, кажется, семантически правильно все таки возвращать при неккоректных входных данных.
