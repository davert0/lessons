package main

import "testing"

func TestQueue(t *testing.T) {
	q := Queue[int]{}

	q.Enqueue(1)
	if q.Size() != 1 {
		t.Error("size should be 1")
	}

	q.Enqueue(2)
	if q.Size() != 2 {
		t.Error("size should be 2")
	}

	res, err := q.Dequeue()
	if err != nil {
		t.Fatal(err)
	}

	if res != 1 {
		t.Error("queue not fifo")
	}

	if q.Size() != 1 {
		t.Error("qeueue not dequeued")
	}
}
