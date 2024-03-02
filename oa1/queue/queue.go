package queue

type Status int

const (
	NotCalled Status = iota
	Ok
	FailEmpty
)

type Queue[T any] interface {
	// команды

	// постусловие - добавлен элемент в начало очереди
	Enqueue(item T)

	// предусловие - очередь не пуста
	//постусловие - убран элемент из начала очереди
	Dequeue()

	// запросы

	Size() int

	// предусловие - очередь не пуста
	GetHead() T
	GetHeadStatus() Status
	DequeueStatus() Status
}

type QueueImpl[T any] struct {
	store         []T
	getHeadStatus Status
	dequeueStatus Status
}

func NewQueue[T any]() *QueueImpl[T] {
	return &QueueImpl[T]{
		store:         make([]T, 0),
		getHeadStatus: NotCalled,
		dequeueStatus: NotCalled,
	}
}

func (q *QueueImpl[T]) Enqueue(item T) {
	q.store = append(q.store, item)
}

func (q *QueueImpl[T]) Dequeue() {
	if q.Size() == 0 {
		q.dequeueStatus = FailEmpty
	}
	q.store = q.store[1:]
	q.dequeueStatus = Ok
}

func (q *QueueImpl[T]) Size() int {
	return len(q.store)
}

func (q *QueueImpl[T]) GetHead() T {
	if q.Size() == 0 {
		q.getHeadStatus = FailEmpty
		return *new(T)
	}
	q.getHeadStatus = Ok
	return q.store[0]
}

func (q *QueueImpl[T]) GetHeadStatus() Status {
	return q.getHeadStatus
}

func (q *QueueImpl[T]) DequeueStatus() Status {
	return q.dequeueStatus
}
