package functionaldesign

func InitializeGame(boardSize int) BoardState {
	initial := BoardState{
		Board: Board{
			Size:  boardSize,
			Cells: makeEmptyBoard(boardSize),
		},
		Score: 0,
	}

	return pipe(
		initial,
		FillEmptySpaces,
		ProcessCascade,
	)
}

func pipe(initial BoardState, fns ...func(BoardState) BoardState) BoardState {
	state := initial
	for _, fn := range fns {
		state = fn(state)
	}
	return state
}

func makeEmptyBoard(size int) [][]Element {
	cells := make([][]Element, size)
	for i := 0; i < size; i++ {
		cells[i] = make([]Element, size)
		for j := 0; j < size; j++ {
			cells[i][j] = Element{Symbol: Empty}
		}
	}
	return cells
}
