package main

import "fmt"

// Поскольку ковариантность в Go не поддерживается, в примере только полиморфизм
// В Go полиморфизм реализуется за счет интерфейсов

type Animal interface {
	Speak() string
}

// Имплементация интерфейса Animal
type Dog struct{}

func (d Dog) Speak() string {
	return "Woof!"
}

// Имплементация интерфейса Animal
type Cat struct{}

func (c Cat) Speak() string {
	return "Meow!"
}

// функция принимающая полиморфный объект
func makeAnimalSpeak(a Animal) {
	fmt.Println(a.Speak())
}

func main() {
	var myAnimal Animal

	myAnimal = Dog{}
	makeAnimalSpeak(myAnimal)

	myAnimal = Cat{}
	makeAnimalSpeak(myAnimal)
}
