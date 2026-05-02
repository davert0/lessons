package main

import (
	"container/list"
	"errors"
	"os"
)

type Queue[T any] struct {
	lst *list.List
}

func (q *Queue[T]) Size() int {
	q.init()
	return q.lst.Len()
}

func (q *Queue[T]) Dequeue() (T, error) {
	q.init()

	var result T
	if q.Size() == 0 {
		return result, errors.New("empty queue")
	}

	res := q.lst.Remove(q.lst.Front())
	result, ok := res.(T)
	if !ok {
		return result, errors.New("unsupported type")
	}

	return result, nil
}

func (q *Queue[T]) Enqueue(itm T) {
	q.init()

	q.lst.PushBack(itm)
}

func (q *Queue[T]) init() {
	if q.lst == nil {
		q.lst = list.New()
	}
}
