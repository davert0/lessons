// 40.1
let rec sum (p, xs) = 
  let rec _sum = function
    | [] -> 0
    | head::tail -> if p head = true then head + _sum tail else _sum tail
  _sum xs

// 40.2.1
let rec count (xs, n) = 
  let rec _count = function
    | [] -> 0
    | head::tail when head > n -> 0
    | head::tail -> if head = n then 1 + _count tail else _count tail
  _count xs

// 40.2.2
let rec insert (xs, n) = 
    let rec _insert cur prev = 
        match cur with
          | [] -> prev @ [n]
          | head::tail when n <= head -> prev @ [n] @ cur
          | head::tail -> _insert tail (prev @ [head])
    _insert xs []

// 40.2.3
let rec intersect (xs1, xs2) = 
  match xs1, xs2 with
    | [], [] -> []
    | [], _ -> []
    | _, [] -> []
    | x::xtail,y::ytail -> if x = y then x::intersect(xtail,ytail) 
                                                       elif x > y then intersect(xs1,ytail)
                                                       else intersect(xtail,xs2)

// 40.2.4
let rec plus (xs1, xs2) = 
  match xs1, xs2 with
    | l1, [] -> l1
    | l1, h2::tail2 -> plus(insert(l1, h2), tail2)

// 40.2.5
let rec minus (xs1, xs2) = 
  match xs1, xs2 with
    | [], [] -> []
    | [], _ -> []
    | x, [] -> x
    | x::xtail,y::ytail -> if x < y then x::minus(xtail,xs2) 
                                                       elif x > y then minus(xs1,ytail)
                                                       else minus(xtail,ytail)

// 40.3.1
let rec smallest lst = 
   let rec _smallest = function
     | x, [] -> None
     | x, [y] when x < y -> Some(x)
     | x, [y] -> Some(y)
     | x, head::tail -> if head < x then _smallest(head, tail) else _smallest(x, tail) 
   _smallest(2147483647, lst)

// 40.3.2
let rec delete (n, xs) = 
  match xs with
    | [] -> []
    | head::tail when head = n -> tail
    | head::tail -> head::delete(n, tail)

// 40.3.3
let rec sort x = 
  let rec _sort (lst1, res) = 
    let m = smallest lst1
    if m.IsSome then _sort(delete(m.Value, lst1), res @ [m.Value])
    else res
  _sort(x, [])

// 40.4
let rec revrev = function
  | [] -> []
  | head::tail -> revrev(tail) @ ([List.rev head])