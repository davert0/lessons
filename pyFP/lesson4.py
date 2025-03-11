from pymonad.tools import curry
from pymonad.maybe import Just
from pymonad.list import ListMonad


@curry(2)
def add(x, y):
    return x + y



def main():
    add10 = add(10)
    print(Just(10).then(add10))
    print(ListMonad(1,2,3).then(add10))
    

if __name__ == "__main__":
    main()