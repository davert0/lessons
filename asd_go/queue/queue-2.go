package main

import "errors"

// Порядковый номер - 5
// Номер задачи - 3
// Краткое название - вращение очереди
// Сложность O(N) - временная, O(1) - пространственная
// Рефлексия - берем остаток от деления для оптимизации (нет смысла делать несколько полных кругов)

func RotateQueue[T any](q *Queue[T], n int) {
	if q.Size() == 0 {
		return
	}

	n = n % q.Size()
	if n < 0 {
		n += q.Size()
	}

	for i := 0; i < n; i++ {
		if val, err := q.Dequeue(); err == nil {
			q.Enqueue(val)
		}
	}
}

// Порядковый номер - 5
// Номер задачи - 4
// Краткое название - очередь на стеках
// Сложность O(N?) - временная, O(N) - пространственная
// Рефлексия - операции dequeue требует перливания из одного стека в другой, что O(N).
// Возможно, амортизированно близко к O(1), я бы проверил банковским методом

type StackQueue[T any] struct {
	stack1 []T
	stack2 []T
}

func (q *StackQueue[T]) Size() int {
	return len(q.stack1) + len(q.stack2)
}

func (q *StackQueue[T]) Dequeue() (T, error) {
	q.init()

	var result T
	if q.Size() == 0 {
		return result, errors.New("empty queue")
	}

	if len(q.stack2) == 0 {
		q.fillStack2()
	}

	last := len(q.stack2) - 1

	result = q.stack2[last]

	q.stack2 = q.stack2[:last]

	return result, nil
}

func (q *StackQueue[T]) Enqueue(itm T) {
	q.init()

	q.stack1 = append(q.stack1, itm)
}

func (q *StackQueue[T]) fillStack2() {
	for i := len(q.stack1) - 1; i >= 0; i-- {
		q.stack2 = append(q.stack2, q.stack1[i])
	}

	q.stack1 = make([]T, 0)
}

func (q *StackQueue[T]) init() {
	if q.stack1 == nil {
		q.stack1 = make([]T, 0)
	}

	if q.stack2 == nil {
		q.stack2 = make([]T, 0)
	}
}

// Порядковый номер - 5
// Номер задачи - 5
// Краткое название - разворот очереди
// Сложность O(N) - временная, O(N) - пространственная
// Рефлексия - разворот делаем за счет буфферного слайса, в который складываем элементы в обратном порядке
func (q *Queue[T]) Reverse() {
	if q.Size() <= 1 {
		return
	}

	stack := make([]T, 0, q.Size())
	for q.Size() > 0 {
		val, _ := q.Dequeue()
		stack = append(stack, val)
	}

	for i := len(stack) - 1; i >= 0; i-- {
		q.Enqueue(stack[i])
	}
}

// Порядковый номер - 5
// Номер задачи - 7
// Краткое название - кольцевая очередь
// Рефлексия - гошные каналы используют кольцевую очередь

type CircularQueue[T any] struct {
	data     []T
	front    int
	rear     int
	capacity int
}

func NewCircularQueue[T any](capacity int) *CircularQueue[T] {
	return &CircularQueue[T]{
		data:     make([]T, capacity),
		front:    -1,
		rear:     -1,
		capacity: capacity,
	}
}

func (q *CircularQueue[T]) isEmpty() bool {
	return len(q.data) == 0
}

func (q *CircularQueue[T]) IsFull() bool {
	return len(q.data) == q.capacity
}

func (q *CircularQueue[T]) Enqueue(item T) error {
	if q.IsFull() {
		return errors.New("queue is full")
	}

	if q.isEmpty() {
		q.front = 0
	}

	q.rear = (q.rear + 1) % q.capacity
	q.data[q.rear] = item
	return nil
}

func (q *CircularQueue[T]) Dequeue() (T, error) {
	var zero T
	if q.isEmpty() {
		return zero, errors.New("queue is empty")
	}

	item := q.data[q.front]
	if q.front == q.rear {
		q.front = -1
		q.rear = -1
	} else {
		q.front = (q.front + 1) % q.capacity
	}
	return item, nil
}

func (q *CircularQueue[T]) Peek() (T, error) {
	var zero T
	if q.isEmpty() {
		return zero, errors.New("queue is empty")
	}
	return q.data[q.front], nil
}
