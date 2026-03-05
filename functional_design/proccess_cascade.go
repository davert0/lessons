package functionaldesign

func ProcessCascade(currentState BoardState) BoardState {
	matches := FindMatches(currentState.Board)
	if len(matches) == 0 {
		return currentState
	}

	return currentState.
	Pipe(func(bs BoardState) BoardState {
		return RemoveMatches(currentState, matches)
	}).
	Pipe(FillEmptySpaces).
	Pipe(ProcessCascade)
}
