from pymonad.tools import curry


# 3.1

@curry(2)
def tag(tag: str, value: str) -> str:
    return f"<{tag}>{value}</{tag}>"

def main():
    bold = tag("b")
    italic = tag("i")
    
    print(bold("hello"))
    print(italic("hello"))
    
if __name__ == "__main__":
    main()
    
    

# 3.2

@curry(3)
def tag(tag: str, attrs: dict, value: str) -> str:
    attrs_str = " ".join([f"{k}=\"{v}\"" for k,v in attrs.items()])
    return f"<{tag} {attrs_str}>{value}</{tag}>"

def main():
    print(tag('li', {'class': 'list-group'}, 'item 23'))

    
if __name__ == "__main__":
    main()
    
    
