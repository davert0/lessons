package main

func Pipe(initial BoardState, fns ...func(BoardState) BoardState) BoardState {
	state := initial
	for _, fn := range fns {
		state = fn(state)
	}
	return state
}
