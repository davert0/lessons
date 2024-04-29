package main

import "fmt"

// Базовый тип Фигура
type Shape interface {
	GetArea() float64
}

// Производный тип Прямоугольник
type Rectangle struct {
	a float64
	b float64
}

func NewRectangle(a float64, b float64) Rectangle {
	return Rectangle{
		a: a,
		b: b,
	}
}

func (r *Rectangle) GetArea() float64 {
	return r.a * r.b
}

// Производный тип Квадрат
type Square struct {
	a float64
}

func NewSquare(a float64) Square {
	return Square{
		a: a,
	}
}

func (r *Square) GetArea() float64 {
	return r.a * r.a
}

func main() {
	// Объявляем массив базового типа Фигура
	var shapes []Shape

	// Добавляем в массив две разные фигуры
	rectangle := NewRectangle(5.0, 6.0)
	shapes = append(shapes, &rectangle)
	square := NewSquare(7.0)
	shapes = append(shapes, &square)

	// Динамическое связывание: вызов методов getArea()
	// для каждого объекта в массиве shapes
	for _, shape := range shapes {
		fmt.Println(shape.GetArea())
	}
}
