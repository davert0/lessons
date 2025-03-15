from pymonad.maybe import Maybe, Nothing, Just


to_left = lambda num: lambda state: (
    Nothing
    if abs((state[0]+num) - state[1]) > 4
    else Just(((state[0]+num), state[1]))
)

to_right = lambda num: lambda state: (
    Nothing
    if abs((state[1]+num) - state[0]) > 4
    else Just((state[0], (state[1]+num)))   
)

banana = lambda x: Nothing

def show(maybe: Maybe):
    print(not maybe.is_nothing())
    
    
begin = lambda: Just((0, 0))


show(
    begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-2))
)

show(
    begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-1))
)

show(
    begin().bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1))
)