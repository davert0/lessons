package main

func ProcessCascade(currentState BoardState) BoardState {
	debugMode := true
	matches := FindMatches(currentState.Board)
	if len(matches) == 0 {
		return currentState
	}

	return currentState.
		Pipe(func(bs BoardState) BoardState {
			return RemoveMatches(currentState, matches)
		}).
		Draw(debugMode).
		Pipe(FillEmptySpaces).
		Draw(debugMode).
		Pipe(ProcessCascade)
}
