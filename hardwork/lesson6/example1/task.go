package taskmanager

type task struct {
	id          int
	name        string
	description string
	priority    Priority
	status      Status
	date        string
}

func (t *task) SetCompleted() error {
	t.status = Complete
	return nil
}

func (t *task) GetName() string {
	return t.name
}

func (t *task) GetDescription() string {
	return t.description
}

func (t *task) GetPriority() Priority {
	return t.priority
}

func (t *task) GetDate() string {
	return t.date
}

func (t *task) GetStatus() Status {
	//TODO implement me
	return t.status
}

func (t *task) GetID() int {
	return t.id
}
