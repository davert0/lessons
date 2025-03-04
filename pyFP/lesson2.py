from pymonad.tools import curry


# 2.3.1. 

@curry(2)
def concat(first: str, second: str):
    return f"{first}{second}"



def main():
    print("2.3.1")
    greeter = concat("Hello, ")
    print(greeter("World"))
    
    
if __name__ == "__main__":
    main()
    
    
# 2.3.2. 

@curry(4)
def concat(greet_word: str, sign: str, name: str, final_sign: str):
    return f"{greet_word}{sign} {name}{final_sign}"


@curry(4)
def first_step(greet_word: str, sign: str, final_sign: str, name: str):
    return concat(greet_word, sign, name, final_sign)


def main():
    print("2.3.2")
    final = first_step("Hello")(",")("!")
    print(final("Petya"))
    
    
if __name__ == "__main__":
    main()
    
    
