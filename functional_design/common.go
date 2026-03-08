package main

import "fmt"

type MatchDirection int

const (
	Horizontal MatchDirection = iota
	Vertical
)

type Match struct {
	Direction MatchDirection
	Row       int
	Col       int
	Length    int
}

const Empty = ' '

var symbols = []rune{'A', 'B', 'C', 'D', 'E'}

type Element struct {
	Symbol rune
}

type Board struct {
	Size  int
	Cells [][]Element
}

type BoardState struct {
	Board Board
	Score int
}

func (s BoardState) Pipe(fn func(BoardState) BoardState) BoardState {
	return fn(s)
}

func (bs BoardState) Draw(ask bool) BoardState {
	board := bs.Board

	fmt.Print("  ")
	for i := 0; i < board.Size; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()

	for i := 0; i < board.Size; i++ {
		fmt.Printf("%d ", i)
		for j := 0; j < board.Size; j++ {
			fmt.Printf("%c ", board.Cells[i][j].Symbol)
		}
		fmt.Println()
	}
	fmt.Println()

	if ask {
		fmt.Scanln()
	}

	return bs
}

func cloneCells(cells [][]Element, size int) [][]Element {
	newCells := make([][]Element, size)
	for i := 0; i < size; i++ {
		newCells[i] = make([]Element, size)
		copy(newCells[i], cells[i])
	}
	return newCells
}
