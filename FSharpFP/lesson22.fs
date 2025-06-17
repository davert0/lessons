type 'a cell = Nil | Cons of 'a * Lazy<'a cell>

let hd (s : 'a cell) : 'a =
  match s with
    Nil -> failwith "hd"
  | Cons (x, _) -> x

let tl (s : 'a cell) : Lazy<'a cell> =
  match s with
    Nil -> failwith "tl"
  | Cons (_, g) -> g

// 51.3
let rec nth (s : 'a cell) (n : int) : 'a = 
   let rec loop iter ls = 
     match (hd ls, tl ls) with
       | (head, tail) when iter = n -> head
       | (head, tail) -> loop (iter + 1) (tail.Force())
   loop 0 s
