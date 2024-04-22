package taskmanager

import "time"

type FileTaskManager struct {
	tasks []Task
}

func (tm *FileTaskManager) AddTask(name string, description string, priority Priority) error {
	for _, t := range tm.tasks {
		if t.GetName() == name {
			return ErrTaskNameAlreadyExist
		}
	}

	task_ := &task{
		name:        name,
		description: description,
		priority:    priority,
		status:      NotComplete,
		date:        time.Now().Format("2006-01-02"),
	}
	id := len(tm.tasks)
	task_.id = id
	tm.tasks = append(tm.tasks, task_)
	return nil
}

func (tm *FileTaskManager) EditTask(id int, name string, description string, priority Priority) error {
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

func (t *FileTaskManager) DeleteTask(id int) error {
	//TODO implement me
	panic("implement me")
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

func main() {

}
