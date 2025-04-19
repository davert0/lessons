// 16.1
let notDivisible (n,m) = m % n = 0

// 16.2
let prime n = 
    match n with
    | _ when n < 2    -> false
    | 2               -> true
    | _ when n % 2 = 0 -> false
    | _ ->
        let limit = int (sqrt (float n))
        let rec loop i =
            match i > limit with
            | true  -> true
            | false ->
                match n % i with
                | 0 -> false
                | _ -> loop (i + 2)
        loop 3