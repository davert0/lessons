package functionaldesign

import "math/rand"

func FillEmptySpaces(currentState BoardState) BoardState {
	if currentState.Board.Cells == nil {
		return currentState
	}

	newCells := cloneCells(currentState.Board.Cells, currentState.Board.Size)

	for row := 0; row < currentState.Board.Size; row++ {
		for col := 0; col < currentState.Board.Size; col++ {
			if newCells[row][col].Symbol == Empty {
				newCells[row][col] = Element{
					Symbol: symbols[rand.Intn(len(symbols))],
				}
			}
		}
	}

	return BoardState{
		Board: Board{
			Size:  currentState.Board.Size,
			Cells: newCells,
		},
		Score: currentState.Score,
	}
}
