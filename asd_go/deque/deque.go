package main

import (
	"container/list"
	"errors"
	"os"
)

type Deque[T any] struct {
	lst *list.List
}

func (d *Deque[T]) Size() int {
	d.init()

	return d.lst.Len()
}

func (d *Deque[T]) AddFront(itm T) {
	d.init()

	d.lst.PushFront(itm)
}

func (d *Deque[T]) AddTail(itm T) {
	d.init()

	d.lst.PushBack(itm)
}

func (d *Deque[T]) RemoveFront() (T, error) {
	var result T
	if d.Size() == 0 {
		return result, errors.New("empty queue")
	}

	untyped := d.lst.Remove(d.lst.Front())
	result, ok := untyped.(T)
	if !ok {
		return result, errors.New("unsupported type")
	}

	return result, nil
}

func (d *Deque[T]) RemoveTail() (T, error) {
	var result T
	if d.Size() == 0 {
		return result, errors.New("empty queue")
	}

	untyped := d.lst.Remove(d.lst.Back())
	result, ok := untyped.(T)
	if !ok {
		return result, errors.New("unsupported type")
	}

	return result, nil
}

func (d *Deque[T]) init() {
	if d.lst == nil {
		d.lst = list.New()
	}
}
