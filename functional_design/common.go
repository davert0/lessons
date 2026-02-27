package functionaldesign

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

func cloneCells(cells [][]Element, size int) [][]Element {
	newCells := make([][]Element, size)
	for i := 0; i < size; i++ {
		newCells[i] = make([]Element, size)
		copy(newCells[i], cells[i])
	}
	return newCells
}
