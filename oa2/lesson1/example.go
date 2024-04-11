package main

import (
	"errors"
	"fmt"
)

var alreadyDeadError = errors.New("Fighter already dead")

type Fighter interface {
	// команды

	// предусловие - боец жив
	// постусловие - здоровье бойца снизилось на величину урона оппонента
	TakeHitFrom(opponent Fighter) error

	// запросы
	GetDamage() int
	GetHealth() int
	IsAlive() bool
}

type Warrior struct {
	health int
	damage int
}

func (f *Warrior) TakeHitFrom(opponent Fighter) error {
	if !f.IsAlive() {
		return alreadyDeadError
	}
	f.health -= opponent.GetDamage()
	return nil
}

func (f *Warrior) GetDamage() int {
	return f.damage
}

func (f *Warrior) GetHealth() int {
	return f.health
}

func (f *Warrior) IsAlive() bool {
	return f.health > 0
}

// композиция
type Knight struct {
	Warrior
}

func NewKnight() Knight {
	return Knight{
		Warrior{
			health: 50,
			damage: 5,
		},
	}
}

// композиция
type Samurai struct {
	Warrior
}

func NewSamurai() Samurai {
	return Samurai{
		Warrior{
			health: 50,
			damage: 7,
		},
	}
}

// полиморфизм
func fight(figther1 Fighter, fighter2 Fighter) bool {
	for figther1.IsAlive() && fighter2.IsAlive() {
		if err := fighter2.TakeHitFrom(figther1); err == nil && fighter2.IsAlive() {
			figther1.TakeHitFrom(fighter2)
		}
	}
	return figther1.IsAlive()
}

func main() {
	chuck := NewKnight()
	bruce := NewKnight()
	carl := NewSamurai()
	dave := NewKnight()
	mark := NewKnight()

	fmt.Println(fight(&chuck, &bruce) == true)
	fmt.Println(fight(&dave, &carl) == false)
	fmt.Println(chuck.IsAlive() == true)
	fmt.Println(bruce.IsAlive() == false)
	fmt.Println(fight(&carl, &mark) == false)
}
