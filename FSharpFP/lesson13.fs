// 39.1
let rec rmodd = function 
    | [] -> []
    | [_] -> []
    | _ :: next :: tail -> next :: rmodd tail
// 39.2
let rec del_even = function 
    | [] -> []
    | head :: tail ->
        if head % 2 = 0 then del_even tail
        else head :: del_even tail

// 39.3
let rec multiplicity x xs = 
    match xs with
     | [] -> 0
     | h::t ->
        (if h = x then 1 else 0) + multiplicity x t 

// 39.4
let rec split = function
    | [] -> ([], [])
    | [x] -> ([x], [])
    | x1::x2::tail ->
        let a, b = split tail
        x1::a, x2::b

exception ListLengthMismatch
// 39.5
let rec zip (xs1,xs2) = 
    if List.length xs1 <> List.length xs2 then raise ListLengthMismatch
    match xs1, xs2 with
    | [], [] -> []
    | h1::t1, h2::t2 -> (h1, h2) :: zip (t1, t2)