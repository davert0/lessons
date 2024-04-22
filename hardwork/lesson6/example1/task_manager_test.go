package taskmanager

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestCreateTaskManager(t *testing.T) {
	taskManager, err := New()
	assert.NotNil(t, taskManager)
	assert.NoError(t, err)
}

func TestNewTaskManagerEmpty(t *testing.T) {
	taskManager, err := New()
	assert.Empty(t, taskManager.GetTasks())
	assert.NoError(t, err)
}

func TestAddTaskNoError(t *testing.T) {
	expected := &task{
		id:          0,
		name:        "test_name",
		description: "test_description",
		priority:    High,
		status:      NotComplete,
		date:        time.Now().Format("2006-01-02"),
	}

	taskManager, _ := New()

	err := taskManager.AddTask("test_name", "test_description", High)
	assert.NoError(t, err)
	assert.Equal(t, 1, len(taskManager.GetTasks()))
	assert.Equal(t, expected, taskManager.GetTasks()[0])

}

func TestAddTaskErrorNameExist(t *testing.T) {
	taskManager, _ := New()

	err := taskManager.AddTask("test_name", "test_description", High)
	assert.NoError(t, err)
	err = taskManager.AddTask("test_name", "test_description", High)
	assert.ErrorIs(t, err, ErrTaskNameAlreadyExist)
}

func TestEditTaskSucces(t *testing.T) {
	taskManager, _ := New()
	edited_name := "test_name_edited"
	taskManager.AddTask("test_name", "test_description", High)
	taskManager.EditTask(0, edited_name, "test_description", High)

	assert.Equal(t, edited_name, taskManager.GetTasks()[0].GetName())
}
