package main

func RemoveMatches(currentState BoardState, matches []Match) BoardState {
	if len(matches) == 0 {
		return currentState
	}

	// Шаг 1: Помечаем ячейки для удаления
	markedCells := markCellsForRemoval(currentState.Board, matches)

	// Шаг 2: Применяем гравитацию
	gravityAppliedCells := applyGravity(markedCells, currentState.Board.Size)

	// Шаг 3: Подсчитываем очки
	removedCount := 0
	for _, m := range matches {
		removedCount += m.Length
	}
	newScore := currentState.Score + calculateScore(removedCount)

	// Возвращаем НОВОЕ состояние
	return BoardState{
		Board: Board{
			Size:  currentState.Board.Size,
			Cells: gravityAppliedCells,
		},
		Score: newScore,
	}
}

func calculateScore(removedCount int) int {
	// Базовая система подсчета очков: 10 за каждый элемент
	return removedCount * 10
}

func markCellsForRemoval(board Board, matches []Match) [][]Element {
	newCells := cloneCells(board.Cells, board.Size)

	for _, match := range matches {
		for i := 0; i < match.Length; i++ {
			row := match.Row
			col := match.Col
			if match.Direction == Horizontal {
				col += i
			} else {
				row += i
			}
			newCells[row][col] = Element{Symbol: Empty}
		}
	}

	return newCells
}

func applyGravity(cells [][]Element, size int) [][]Element {
	newCells := make([][]Element, size)
	for row := 0; row < size; row++ {
		newCells[row] = make([]Element, size)
		for col := 0; col < size; col++ {
			newCells[row][col] = Element{Symbol: Empty}
		}
	}

	for col := 0; col < size; col++ {
		newRow := size - 1
		for row := size - 1; row >= 0; row-- {
			if cells[row][col].Symbol != Empty {
				newCells[newRow][col] = cells[row][col]
				newRow--
			}
		}
	}

	return newCells
}

