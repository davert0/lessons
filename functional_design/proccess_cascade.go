package functionaldesign

func ProcessCascade(currentState BoardState) BoardState {
	matches := FindMatches(currentState.Board)
	if len(matches) == 0 {
		return currentState
	}

	newState := RemoveMatches(currentState, matches)
	newState = FillEmptySpaces(newState)
	return ProcessCascade(newState)
}
