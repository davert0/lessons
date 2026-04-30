package main

func RotateQueue[T any](q *Queue[T], n int) error {
	if q.Size() == 0 || q.Size() == 1 {
		return nil
	}

	for range n {
		el, err := q.Dequeue()
		if err != nil {
			return err
		}

		q.Enqueue(el)
	}

	return nil
}
