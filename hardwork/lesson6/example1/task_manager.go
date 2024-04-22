package taskmanager

import (
	"slices"
	"time"
)

type FileTaskManager struct {
	tasks []Task
}

func (tm *FileTaskManager) AddTask(name string, description string, priority Priority) error {
	ids := make([]int, 0, len(tm.tasks))

	for _, t := range tm.tasks {
		if t.GetName() == name {
			return ErrTaskNameAlreadyExist
		}
		ids = append(ids, t.GetID())
	}
	task_ := &task{
		name:        name,
		description: description,
		priority:    priority,
		status:      NotComplete,
		date:        time.Now().Format("2006-01-02"),
	}

	id := 0
	if len(ids) > 0 {
		id = slices.Max(ids) + 1
	}
	task_.id = id
	tm.tasks = append(tm.tasks, task_)
	return nil
}

func (tm *FileTaskManager) EditTask(id int, name string, description string, priority Priority) error {
	if id < 0 || id >= len(tm.tasks) {
		return ErrTaskNotFound
	}

	t := tm.tasks[id]
	t = &task{
		id:          id,
		name:        name,
		description: description,
		priority:    0,
		status:      t.GetStatus(),
		date:        t.GetDate(),
	}
	tm.tasks[id] = t
	return nil
}

func (tm *FileTaskManager) DeleteTask(id int) error {
	for i, t := range tm.tasks {
		if t.GetID() == id {
			tm.tasks = append(tm.tasks[:i], tm.tasks[i+1:]...)
			return nil
		}
	}
	return ErrTaskNotFound
}

func (t *FileTaskManager) SetTaskCompleted(id int) error {
	//TODO implement me
	panic("implement me")
}

func (t *FileTaskManager) GetTasks() []Task {
	return t.tasks
}

func New() (TaskManager, error) {
	return &FileTaskManager{}, nil
}
