package main

import (
	"fmt"
)

// Наследование реализиации также доступно за счет встраивания структур, однако сам язык подталкивает к плоской иерархии

// Базовая реализация
type Base struct {
	name string
}

func (b *Base) SetName(name string) {
	b.name = name
}

func (b *Base) GetName() string {
	return b.name
}

// Расширенная реализация
type Extended struct {
	Base  // встраивание структуры Base
	level int
}

func (e *Extended) SetLevel(level int) {
	e.level = level
}

func (e *Extended) GetLevel() int {
	return e.level
}

func ImplementationEmbedding() {
	e := &Extended{}
	e.SetName("Example")
	e.SetLevel(10)

	fmt.Println("Name:", e.GetName())
	fmt.Println("Level:", e.GetLevel())
}

// Льготное встриавание
// Общая структура для обработки исключений, реализует интерфейс error
type CustomError struct {
	Code    int
	Message string
}

func (e *CustomError) Error() string {
	return fmt.Sprintf("Error %d: %s", e.Code, e.Message)
}

// Частное использование CustomError
type NotFoundError struct {
	CustomError // льготное наследование
}

func NewNotFoundError(message string) error {
	return &NotFoundError{
		CustomError: CustomError{
			Code:    404,
			Message: message,
		},
	}
}

func FacilityEmbedding() {
	err := NewNotFoundError("Resource not found")
	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	ImplementationEmbedding()
	FacilityEmbedding()
}
