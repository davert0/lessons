package lesson9

import (
	"encoding/json"
	"fmt"
	"reflect"
)

// General - базовый интерфейс с фундаментальными операциями
type General interface {
	Copy(src General)
	DeepCopy() General
	Clone() General
	Equals(other General) bool
	DeepEquals(other General) bool
	String() string
	GetType() reflect.Type
	IsType(t reflect.Type) bool
}

// Any - структура, реализующая интерфейс General
type Any struct{}

func (a *Any) Copy(src General) {
	// Реализация копирования содержимого одного объекта в другой
	*a = *(src.(*Any))
}

func (a *Any) DeepCopy() General {
	// Реализация глубокого копирования объекта
	copy := &Any{}
	*copy = *a
	return copy
}

func (a *Any) Clone() General {
	// Реализация клонирования объекта
	return a.DeepCopy()
}

func (a *Any) Equals(other General) bool {
	// Реализация сравнения объектов
	return reflect.DeepEqual(a, other)
}

func (a *Any) DeepEquals(other General) bool {
	// Реализация глубокого сравнения объектов
	return reflect.DeepEqual(a, other)
}

func (a *Any) String() string {
	// Реализация преобразования объекта в строку
	str, _ := json.Marshal(a)
	return string(str)
}

func (a *Any) GetType() reflect.Type {
	// Получение реального типа объекта
	return reflect.TypeOf(a).Elem()
}

func (a *Any) IsType(t reflect.Type) bool {
	// Проверка типа объекта
	return a.GetType() == t
}

func main() {
	obj1 := &Any{}
	obj2 := &Any{}

	fmt.Println("obj1 == obj2:", obj1.Equals(obj2))
	fmt.Println("obj1 type:", obj1.GetType())
	fmt.Println("obj1 is *Any:", obj1.IsType(reflect.TypeOf(&Any{})))

	clone := obj1.Clone()
	fmt.Println("clone == obj1:", clone.Equals(obj1))
}
