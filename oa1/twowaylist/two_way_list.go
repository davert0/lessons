package twowaylist

import "fmt"

const (
	CursorMoveStatusNil          CursorMoveStatus = 0
	CursorMoveStatusOk           CursorMoveStatus = 1
	CursorMoveStatusErrListEmpty CursorMoveStatus = 2
	CursorMoveStatusErrNoRight   CursorMoveStatus = 3
	CursorMoveStatusErrNoLeft    CursorMoveStatus = 4
)

const (
	GetValueStatusNil    GetValueStatus = 0
	GetValueStatusOk     GetValueStatus = 1
	GetValueErrEmptyList GetValueStatus = 2
)

const (
	PutStatusNil PutStatus = 0
	PutStatusOk  PutStatus = 1
)

const (
	FindStatusNil          FindStatus = 0
	FindStatusOk           FindStatus = 1
	FindStatusErrListEmpty FindStatus = 2
	FindStatusErrNotFound  FindStatus = 3
)

const (
	RemoveAllStatusNil          RemoveAllStatus = 0
	RemoveAllStatusOk           RemoveAllStatus = 1
	RemoveAllStatusErrListEmpty RemoveAllStatus = 2
	RemoveAllStatusErrNotFound  RemoveAllStatus = 3
)

const (
	RemoveStatusNil          RemoveStatus = 0
	RemoveStatusOk           RemoveStatus = 1
	RemoveStatusErrListEmpty RemoveStatus = 2
)

const (
	ReplaceStatusNil          ReplaceStatus = 0
	ReplaceStatusOk           ReplaceStatus = 1
	ReplaceStatusErrListEmpty ReplaceStatus = 2
)

type (
	CursorMoveStatus int
	GetValueStatus   int
	PutStatus        int
	FindStatus       int
	RemoveAllStatus  int
	RemoveStatus     int
	ReplaceStatus    int
	CursorPosition   int
)

type IParentList[T comparable] interface {
	//queries

	// предусловие - список не пустой
	Get() *T

	Size() int

	IsHead() bool

	IsTail() bool

	IsValue() bool

	GetCursorMoveStatus() CursorMoveStatus
	GetValueStatus() GetValueStatus
	GetPutStatus() PutStatus
	GetFindStatus() FindStatus
	GetRemoveAllStatus() RemoveAllStatus
	GetRemoveStatus() RemoveStatus
	GetReplaceStatus() ReplaceStatus

	//commands

	// предусловие - список не пустой
	// постусловие - курсор в начале списка
	Head()

	// предусловие - список не пустой
	// постусловие - курсор в конце списка
	Tail()

	// предусловие - справа есть элементы
	// постусловие - курсор сдвинут на элемент вправо
	Right()

	// предусловие - список не пустой
	// постусловие - курсор установлен на следующий справа искомый элемент
	Find(value T)

	// постусловие - в список добавляется элемент справа от текущего
	PutRight(value T)

	// постусловие - в список добавляется элемент слева от текущего
	PutLeft(value T)

	// предусловие: список не пуст;
	// постусловие: текущий узел удалён,
	// курсор смещён к правому соседу, если он есть,
	// в противном случае курсор смещён к левому соседу,
	// если он есть
	Remove()

	// постусловие - список пустой
	Clear()

	// постусловие - в хвост добавляется элемент
	AddTail(value T)

	// предусловие - список не пустой
	// постусловие - текущий элемент заменяется на переданный
	Replace(value T)

	// предусловие - список не пустой
	// постусловие - удалены все элементы с переданным значением из списка
	RemoveAll(value T)
}

type ITwoWayList[T comparable] interface {
	IParentList[T]

	// предусловие - слева есть элементы
	// постусловие - курсор сдвинут влево
	Left()
}

type ILinkedList[T comparable] interface {
	IParentList[T]
}

type ParentList[T comparable] struct {
	list             []T
	cursorPosition   CursorPosition
	cursorMoveStatus CursorMoveStatus
	getValueStatus   GetValueStatus
	putStatus        PutStatus
	findStatus       FindStatus
	removeAllStatus  RemoveAllStatus
	removeStatus     RemoveStatus
	replaceStatus    ReplaceStatus
}

func (p *ParentList[T]) Get() *T {
	if !p.IsValue() {
		p.getValueStatus = GetValueErrEmptyList
		return nil
	}
	el := p.list[p.cursorPosition]
	p.getValueStatus = GetValueStatusOk
	return &el
}

func (p *ParentList[T]) Size() int {
	return len(p.list)
}

func (p *ParentList[T]) IsHead() bool {
	if !p.IsValue() {
		return false
	}
	return p.cursorPosition == 0
}

func (p *ParentList[T]) IsTail() bool {
	if !p.IsValue() {
		return false
	}
	return int(p.cursorPosition) == len(p.list)-1
}

func (p *ParentList[T]) IsValue() bool {
	return len(p.list) > 0
}

func (p *ParentList[T]) GetCursorMoveStatus() CursorMoveStatus {
	return p.cursorMoveStatus
}

func (p *ParentList[T]) GetValueStatus() GetValueStatus {
	return p.getValueStatus
}

func (p *ParentList[T]) GetPutStatus() PutStatus {
	return p.putStatus
}

func (p *ParentList[T]) GetFindStatus() FindStatus {
	return p.findStatus
}

func (p *ParentList[T]) GetRemoveAllStatus() RemoveAllStatus {
	return p.removeAllStatus
}

func (p *ParentList[T]) GetRemoveStatus() RemoveStatus {
	return p.removeStatus
}

func (p *ParentList[T]) GetReplaceStatus() ReplaceStatus {
	return p.replaceStatus
}

func (p *ParentList[T]) Head() {
	if len(p.list) == 0 {
		p.cursorMoveStatus = CursorMoveStatusErrListEmpty
		return
	}
	p.cursorMoveStatus = CursorMoveStatusOk
	p.cursorPosition = 0
}

func (p *ParentList[T]) Tail() {
	if !p.IsValue() {
		p.cursorMoveStatus = CursorMoveStatusErrListEmpty
		return
	}
	p.cursorMoveStatus = CursorMoveStatusOk
	p.cursorPosition = CursorPosition(len(p.list) - 1)
}

func (p *ParentList[T]) Right() {
	if !p.IsValue() {
		p.cursorMoveStatus = CursorMoveStatusErrListEmpty
		return
	}
	if p.IsTail() {
		p.cursorMoveStatus = CursorMoveStatusErrNoRight
		return
	}
	p.cursorMoveStatus = CursorMoveStatusOk
	p.cursorPosition = p.cursorPosition + 1
	return
}

func (p *ParentList[T]) Find(value T) {
	if p.IsTail() {
		p.findStatus = FindStatusErrListEmpty
		return
	}
	for i, _ := range p.list {
		if p.list[i] == value {
			p.findStatus = FindStatusOk
			p.cursorPosition = CursorPosition(i)
			return
		}
	}
	p.findStatus = FindStatusErrNotFound
	return
}

func (p *ParentList[T]) PutRight(value T) {
	if !p.IsValue() {
		p.list = append(p.list, value)
		p.putStatus = PutStatusOk
		return
	}
	p.list = insert(p.list, int(p.cursorPosition)+1, value)
	p.putStatus = PutStatusOk
}

func (p *ParentList[T]) PutLeft(value T) {
	if !p.IsValue() {
		p.list = append(p.list, value)
		p.putStatus = PutStatusOk
		return
	}
	p.list = insert(p.list, int(p.cursorPosition)-1, value)
	p.putStatus = PutStatusOk
}
func (p *ParentList[T]) Remove() {
	if !p.IsValue() {
		p.removeStatus = RemoveStatusErrListEmpty
		return
	}
	if !p.IsTail() {
		p.list = removeElement(p.list, int(p.cursorPosition))
		p.removeStatus = RemoveStatusOk
		return
	}
	p.list = removeElement(p.list, int(p.cursorPosition))
	p.removeStatus = RemoveStatusOk
	p.cursorPosition = CursorPosition(len(p.list))
}

func (p *ParentList[T]) Clear() {
	p.list = p.list[:0]
}

func (p *ParentList[T]) AddTail(value T) {
	p.list = append(p.list, value)
	p.putStatus = PutStatusOk
}

func (p *ParentList[T]) RemoveAll(value T) {
	for i, _ := range p.list {
		if p.list[i] == value {
			p.Remove()
		}
	}
	p.removeAllStatus = RemoveAllStatusOk
	return
}

func (p *ParentList[T]) Replace(value T) {
	if !p.IsValue() {
		p.replaceStatus = ReplaceStatusErrListEmpty
		return
	}
	p.list[p.cursorPosition] = value
	p.replaceStatus = ReplaceStatusOk
}

type TwoWayList[T comparable] struct {
	ParentList[T]
}

// предусловие - слева есть элементы
// постусловие - курсор сдвинут влево
func (l *TwoWayList[T]) Left() {
	if !l.IsValue() {
		l.cursorMoveStatus = CursorMoveStatusErrListEmpty
		return
	}
	if l.IsHead() {
		l.cursorMoveStatus = CursorMoveStatusErrNoLeft
		return
	}
	l.cursorMoveStatus = CursorMoveStatusOk
	l.cursorPosition = l.cursorPosition + 1
	return
}

type LinkedList[T comparable] interface {
	ParentList[T]
}

func insert[T any](slice []T, index int, value T) []T {
	if index > len(slice) {
		fmt.Println("Error: Index out of range")
		return slice
	}
	if index < 0 {
		index = 0
	}

	slice = append(slice[:index], append([]T{value}, slice[index:]...)...)

	return slice
}

func removeElement[T any](slice []T, index int) []T {
	if index < 0 || index >= len(slice) {
		fmt.Println("Error: Index out of range")
		return slice
	}
	return append(slice[:index], slice[index+1:]...)
}
