package functionaldesign

func InitializeGame(boardSize int) BoardState {
	return BoardState{
		Board: Board{
			Size:  boardSize,
			Cells: makeEmptyBoard(boardSize),
		},
		Score: 0,
	}.
		Pipe(FillEmptySpaces).
		Pipe(ProcessCascade)
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
