package main

import "fmt"

// в Go запрета на переопределение методов можно достичь за счет вызова приватного метода из публичного.
// Тогда при встраивании и переопределении приватного метода в потомке, вызываться будет метод родительской структуры

type Parent struct{}

func (p *Parent) Public() {
	p.private()
}

func (p *Parent) private() {
	fmt.Println("This is a parent method")
}

type Child struct {
	Parent
}

func (p *Child) private() {
	fmt.Println("This is a child method")
}

func main() {
	parent := Parent{}
	child := Child{}

	// "This is a parent method"
	parent.Public()
	// "This is a parent method"
	child.Public()
}
