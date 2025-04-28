let curry f = 
  let g (x: int) =
    let h (y: int) : int = f(x,y)
    h
  g

let uncurry f =
  let g (x: int, y: int) : int = 
    let h = f x
    h y
  g