package functionaldesign

func FindMatches(board Board) []Match {
	var matches []Match

	// Горизонтальные комбинации
	for row := 0; row < board.Size; row++ {
		startCol := 0
		for col := 1; col < board.Size; col++ {
			// Пропускаем пустые ячейки в начале строки
			if board.Cells[row][startCol].Symbol == Empty {
				startCol = col
				continue
			}
			// Если текущая ячейка пустая, обрываем текущую последовательность
			if board.Cells[row][col].Symbol == Empty {
				matches = addMatchIfValid(matches, row, startCol, col-startCol, Horizontal)
				startCol = col + 1
				continue
			}
			// Проверяем совпадение символов для непустых ячеек
			if board.Cells[row][col].Symbol != board.Cells[row][startCol].Symbol {
				matches = addMatchIfValid(matches, row, startCol, col-startCol, Horizontal)
				startCol = col
			} else if col == board.Size-1 {
				matches = addMatchIfValid(matches, row, startCol, col-startCol+1, Horizontal)
			}
		}
	}

	// Вертикальные комбинации
	for col := 0; col < board.Size; col++ {
		startRow := 0
		for row := 1; row < board.Size; row++ {
			// Пропускаем пустые ячейки в начале столбца
			if board.Cells[startRow][col].Symbol == Empty {
				startRow = row
				continue
			}
			// Если текущая ячейка пустая, обрываем текущую последовательность
			if board.Cells[row][col].Symbol == Empty {
				matches = addMatchIfValid(matches, startRow, col, row-startRow, Vertical)
				startRow = row + 1
				continue
			}
			// Проверяем совпадение символов для непустых ячеек
			if board.Cells[row][col].Symbol != board.Cells[startRow][col].Symbol {
				matches = addMatchIfValid(matches, startRow, col, row-startRow, Vertical)
				startRow = row
			} else if row == board.Size-1 {
				matches = addMatchIfValid(matches, startRow, col, row-startRow+1, Vertical)
			}
		}
	}

	return matches
}

func addMatchIfValid(matches []Match, row, col, length int, direction MatchDirection) []Match {
	// Учитываем только комбинации из 3 и более элементов (ТЗ)
	if length >= 3 {
		matches = append(matches, Match{
			Direction: direction,
			Row:       row,
			Col:       col,
			Length:    length,
		})
	}
	return matches
}
