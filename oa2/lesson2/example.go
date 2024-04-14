package main

import "fmt"

type Car struct {
	maxSpeedKMH int
}

func NewCar() Car {
	return Car{maxSpeedKMH: 100}
}

func (c Car) Drive() {
	fmt.Printf("Going with %v speed \n", c.maxSpeedKMH)
}

type Truck struct {
	Car
	// расширение родителя
	maxLoadKG int
}

func NewTruck() Truck {
	return Truck{
		// специализация родителя
		Car:       Car{maxSpeedKMH: 50},
		maxLoadKG: 3000,
	}
}

// расширение родителя
func (t Truck) Load() {
	fmt.Printf("Loading the truck with max load %v \n", t.maxLoadKG)
}

func main() {
	truck := NewTruck()
	truck.Drive()
	truck.Load()
}
