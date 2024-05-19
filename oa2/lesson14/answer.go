package main

type General interface {
	Add(other General) General
}

// Реализуем тип Vector с поддержкой generics.
type Vector[T General] struct {
	elements []T
}

// Add складывает два вектора одинаковой длины.
func (v Vector[T]) Add(other Vector[T]) *Vector[T] {
	if len(v.elements) != len(other.elements) {
		return nil
	}
	result := make([]T, len(v.elements))
	for i, val := range v.elements {
		result[i] = val.Add(other.elements[i]).(T)
	}
	return &Vector[T]{elements: result}
}

// Пример реализации произвольного типа, который будет использоваться как элемент вектора.
type IntElement int

func (a IntElement) Add(b General) General {
	return a + b.(IntElement)
}
