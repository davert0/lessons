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
	//TODO implement me
	panic("implement me")
}

func (t *task) GetName() string {
	return t.name
}

func (t *task) GetDescription() string {
	//TODO implement me
	panic("implement me")
}

func (t *task) GetPriority() Priority {
	//TODO implement me
	panic("implement me")
}

func (t *task) GetDate() string {
	return t.date
}

func (t *task) GetStatus() Status {
	//TODO implement me
	return t.status
}
