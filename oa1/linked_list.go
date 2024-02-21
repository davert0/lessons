package oa1

const (
	CursorMoveStatusNil = iota
	CursorMoveStatusOk
	CursorMoveStatusErrListEmpty
	CursorMoveStatusErrNoRight
)

const (
	GetValueStatusNil = iota
	GetValueStatusOk
	GetValueErrEmptyList
)

const (
	PutStatusNil = iota
	PutStatusOk
)

const (
	FindStatusNil = iota
	FindStatusOk
	FindStatusErrListEmpty
	FindStatusErrNotFound
)

const (
	RemoveAllStatusNil = iota
	RemoveAllStatusOk
	RemoveAllStatusErrListEmpty
	RemoveAllStatusErrNotFound
)

const (
	RemoveStatusNil = iota
	RemoveStatusOk
	RemoveStatusErrListEmpty
)

const (
	ReplaceStatusNil = iota
	ReplaceStatusOk
	ReplaceStatusErrListEmpty
)

type LinkedList[T any] interface {
	//queries

	// предусловие - список не пустой
	Get()

	Size()

	IsHead()

	IsTail()

	IsValue()

	GetCursorMoveStatus()
	GetValueStatus()
	GetPutStatus()
	GetFindStatus()
	GetRemoveAllStatus()
	GetRemoveStatus()
	GetReplaceStatus()

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
	Find(T)

	// постусловие - в список добавляется элемент справа от текущего
	PutRight(T)

	// постусловие - в список добавляется элемент слева от текущего
	PutLeft(T)

	// предусловие - список не пустой
	// постусловие - курсор смещается к правому соседу, если он есть, иначе к левому
	Remove()

	// постусловие - список пустой
	Clear()

	// постусловие - в хвост добавляется элемент
	AddTail(T)

	// предусловие - список не пустой
	// постусловие - текущий элемент заменяется на переданный
	Replace(T)

	// предусловие - список не пустой
	// постусловие - удалены все элементы с переданным значением из списка
	RemoveAll(T)
}
