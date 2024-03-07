package queue

type Status int

const (
	NotCalled Status = iota
	Ok
	FailEmpty
)

type Queue[T any] interface {
	// команды

	// постусловие - добавлен элемент в конец очереди
	EnqueueTail(item T)

	// предусловие - очередь не пуста
	//постусловие - убран элемент из начала очереди
	DequeueHead()

	// запросы

	Size() int

	// предусловие - очередь не пуста
	GetHead() T

	GetHeadStatus() Status
	DequeueHeadStatus() Status
}

type Deque[T any] interface {
	Queue[T]

	// команды

	// постусловие - добавлен элемент в начало очереди
	EnqueueHead(item T)

	// предусловие - очередь не пуста
	//постусловие - убран элемент из конца очереди
	DequeueTail()

	// запросы

	//предусловие - очередь не пуста
	GetTail() T
	GetTailStatus() Status
	DequeueTailStatus() Status
}

type QueueImpl[T any] struct {
	store             []T
	getHeadStatus     Status
	dequeueHeadStatus Status
}

func NewQueue[T any]() *QueueImpl[T] {
	return &QueueImpl[T]{
		store:             make([]T, 0),
		getHeadStatus:     NotCalled,
		dequeueHeadStatus: NotCalled,
	}
}

func (q *QueueImpl[T]) EnqueueTail(item T) {
	q.store = append(q.store, item)
}

func (q *QueueImpl[T]) DequeueHead() {
	if q.Size() == 0 {
		q.dequeueHeadStatus = FailEmpty
	}
	q.store = q.store[1:]
	q.dequeueHeadStatus = Ok
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

func (q *QueueImpl[T]) DequeueHeadStatus() Status {
	return q.dequeueHeadStatus
}

type DequeImpl[T any] struct {
	QueueImpl[T]
	getTailStatus     Status
	dequeueTailStatus Status
}

func NewDeque[T any]() *DequeImpl[T] {
	return &DequeImpl[T]{
		QueueImpl: QueueImpl[T]{
			store:             make([]T, 0),
			getHeadStatus:     NotCalled,
			dequeueHeadStatus: NotCalled,
		},
		getTailStatus:     NotCalled,
		dequeueTailStatus: NotCalled,
	}
}

func (d *DequeImpl[T]) EnqueueHead(item T) {
	d.store = append([]T{item}, d.store...)
}

// предусловие - очередь не пуста
// постусловие - убран элемент из конца очереди
func (d *DequeImpl[T]) DequeueTail() {
	if d.Size() == 0 {
		d.dequeueTailStatus = FailEmpty
	}
	d.store = d.store[:len(d.store)-1]
	d.dequeueTailStatus = Ok
}

// запросы

func (d *DequeImpl[T]) GetTail() T {
	if d.Size() == 0 {
		d.getTailStatus = FailEmpty
		return *new(T)
	}
	d.getTailStatus = Ok
	return d.store[0]
}

func (q *DequeImpl[T]) GetTailStatus() Status {
	return q.getTailStatus
}

func (q *DequeImpl[T]) DequeueTailStatus() Status {
	return q.dequeueTailStatus
}
