package oa1

const (
	PopNil         = 0
	PopOk          = 1
	PopErr         = 2
	PeekNil        = 0
	PeekOk         = 1
	PeekErr        = 2
	PushNil        = 0
	PushOk         = 1
	PushErr        = 2
	DefaultMaxSize = 32
)

type BoundedStack[T any] struct {
	stack      []T
	peekStatus int
	popStatus  int
	pushStatus int
	maxSize    int
}

// предусловие - maxElemnts >= 1
// постусловие - создан новый стек с размером MaxElements
func NewBoundedStackWithOptions[T any](maxSize int) *BoundedStack[T] {
	if maxSize < 1 {
		panic("max elements should be >= 1")
	}
	bs := &BoundedStack[T]{
		stack:      make([]T, 0, maxSize),
		peekStatus: PeekNil,
		popStatus:  PopNil,
		pushStatus: PushNil,
		maxSize:    maxSize,
	}
	bs.Clear()
	return bs
}

// постусловие - создан стек с размером DefaultMaxSize
func NewBoundedStack[T any]() *BoundedStack[T] {
	return &BoundedStack[T]{
		stack:      make([]T, 0, DefaultMaxSize),
		peekStatus: PeekNil,
		popStatus:  PopNil,
		pushStatus: PushNil,
		maxSize:    DefaultMaxSize,
	}
}

// предусловие - стек не пустой
func (bs *BoundedStack[T]) Peek() *T {
	if bs.Size() == 0 {
		bs.peekStatus = PeekErr
		return nil
	}
	result := bs.stack[len(bs.stack)-1]
	bs.peekStatus = PeekOk
	return &result
}

// предусловие - стек не заполнен
// постусловие - в стек добавлено новое значение
func (bs *BoundedStack[T]) Push(value T) {
	if len(bs.stack) >= bs.maxSize {
		bs.pushStatus = PushErr
		return
	}
	bs.stack = append(bs.stack, value)
	bs.pushStatus = PushOk
}

// предусловие - стек не пустой
// постусловие - со стека снимается верхний элемент
func (bs *BoundedStack[T]) Pop() {
	if bs.Size() == 0 {
		bs.popStatus = PopErr
		return
	}
	bs.stack = bs.stack[:len(bs.stack)-1]
	bs.popStatus = PopOk
}

func (bs *BoundedStack[T]) Clear() {
	bs.stack = make([]T, 0, bs.maxSize)
	bs.peekStatus = PeekNil
	bs.popStatus = PopNil
	bs.pushStatus = PushNil
}

func (bs *BoundedStack[T]) Size() int {
	return len(bs.stack)
}
func (bs *BoundedStack[T]) GetPopStatus() int {
	return bs.popStatus
}

func (bs *BoundedStack[T]) GetPeekStatus() int {
	return bs.peekStatus
}

func (bs *BoundedStack[T]) GetPushStatus() int {
	return bs.pushStatus
}
