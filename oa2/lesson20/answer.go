package main

import (
	"fmt"
)

// Наследование вариаций - в Go - встраивание родительской структуры и переопределение ее методов

// Базовая структура
type Human struct {
	Name string
	Age  int
}

// Метод, который будет переопределяться
func (h Human) Greet() {
	fmt.Printf("Hello, I am %s.\n", h.Name)
}

// Мужчина (Male) - переопределение метода без изменения сигнатуры (Functional Variation Inheritance)
type Male struct {
	Human // Встраиваем Human
}

func (m Male) Greet() {
	fmt.Printf("Hi there, I am Mr. %s.\n", m.Name)
}

// Женщина (Female) - переопределение метода с изменением сигнатуры (Type Variation Inheritance)
type Female struct {
	Human // Встраиваем Human
}

func (f Female) Greet(greeting string) {
	fmt.Printf("%s, I am Mrs. %s.\n", greeting, f.Name)
}

func variationEmbedding() {
	h := Human{Name: "Alex", Age: 30}
	h.Greet()

	m := Male{Human{Name: "John", Age: 25}}
	m.Greet()

	f := Female{Human{Name: "Jane", Age: 22}}
	f.Greet("Good afternoon")
}

// Наследование с конкретизацией - в Go - имплементация интерфейсов

// Абстрактный интерфейс
type Shape interface {
	Area() float64
	Perimeter() float64
}

// Конкретная реализация (структура Круг)
type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return 3.14 * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
	return 2 * 3.14 * c.Radius
}

// Конкретная реализация (структура Прямоугольник)
type Rectangle struct {
	Width, Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return 2 * (r.Width + r.Height)
}

func PrintShapeInfo(s Shape) {
	fmt.Printf("Area: %f, Perimeter: %f\n", s.Area(), s.Perimeter())
}

func reificationImplementation() {
	c := Circle{Radius: 5}
	r := Rectangle{Width: 4, Height: 6}

	PrintShapeInfo(c)
	PrintShapeInfo(r)
}

// Структурное наследование - в Go также реализуется через имплементацию служебных интерфейсов

// Интерфейс для сравнения
type Comparable interface {
	CompareTo(other Comparable) int
}

// Структура, реализующая интерфейс Comparable
type Car struct {
	Brand string
	Year  int
}

func (c Car) CompareTo(other Comparable) int {
	otherCar := other.(Car)
	if c.Year > otherCar.Year {
		return 1
	} else if c.Year < otherCar.Year {
		return -1
	} else {
		return 0
	}
}

func structureImplementation() {
	c1 := Car{Brand: "Toyota", Year: 2010}
	c2 := Car{Brand: "Honda", Year: 2015}

	comparison := c1.CompareTo(c2)
	if comparison == 0 {
		fmt.Println("Cars are of the same year.")
	} else if comparison > 0 {
		fmt.Println("Car 1 is newer than Car 2.")
	} else {
		fmt.Println("Car 1 is older than Car 2.")
	}
}

func main() {
	variationEmbedding()
	reificationImplementation()
	structureImplementation()
}
