package main

import (
	"fmt"
)

// в Go функциональность мииксинов можно реализовать за счет встраивания интерфейсов

type Yeller interface {
	Yell(message string)
}

// Функция Yell может работать только с объектами, реализующмии интерфейс Yeller
func Yell(y Yeller, message string) {
	y.Yell(message)
}

type Whisperer interface {
	Whisper(message string)
}

// Функция Whisper может работать только с объектами, реализующмии интерфейс Whisperer
func Whisper(w Whisperer, message string) {
	w.Whisper(message)
}

// Структуры Person и Robot не реализуют интерфейс напрямую, но мы можем встроить в них имплементации
type Person struct {
	Yeller
	Whisperer
}
type Robot struct {
	Yeller
	Whisperer
}

// имплементации интерфейсов
type yeller string

func (y yeller) Yell(message string) {
	fmt.Printf(string(y), message)
}

type twiceYeller string

func (twice twiceYeller) Yell(message string) {
	fmt.Printf(string(twice+twice), message, message)
}

type whisperer string

func (w whisperer) Whisper(message string) {
	fmt.Printf(string(w), message)
}

func main() {
	Yell(&Person{Yeller: yeller("%s!!!\n")}, "Nooooo")
	Yell(&Robot{Yeller: twiceYeller("*** %s ***")}, "Oh no")
	Whisper(&Person{Whisperer: whisperer("Sssssh! %s!\n")}, "...")
	Whisper(&Robot{Whisperer: whisperer("Sssssh! %s!\n")}, "...")
}
