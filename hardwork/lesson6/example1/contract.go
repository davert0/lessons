package taskmanager

import (
	"errors"
)

const (
	High Priority = iota
	Mid
	Low
)

const (
	NotComplete Status = iota
	Complete
)

type Priority int64
type Status int64

var ErrTaskNameAlreadyExist = errors.New("task with that name already exist")

//Приложение должно позволять пользователю управлять списком задач.

type TaskManager interface {
	// команды

	// предусловие - не существует задачи с таким же именем
	// постусловие - задача добавлена в список задач
	AddTask(name string, description string, priority Priority) error

	// предусловие - задача с данным ID существует в списке
	// постусловие - задача изменена
	EditTask(id int, name string, description string, priority Priority) error

	// предусловие - задача с данным ID существует в списке
	// постусловие - задача удалена из списка
	DeleteTask(id int) error

	// предусловие - задача с данным ID существует в списке
	// постусловие - задача помечается как выполненная
	SetTaskCompleted(id int) error

	// запросы

	GetTasks() []Task
}

// Каждая задача имеет название, описание, приоритет (высокий, средний, низкий), дату создания и статус (выполнена или нет).
type Task interface {
	// команды
	SetCompleted() error

	// запросы

	GetName() string
	GetDescription() string
	GetPriority() Priority
	GetDate() string
	GetStatus() Status
}
