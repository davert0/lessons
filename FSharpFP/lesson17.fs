// 43.3
let try_find key m = 
  if Map.containsKey key m = false then None
  else 
    let lst = Map.toList m
    let rec search ls =
      match ls with
      | [] -> None
      | (k, v) :: tail when k = key -> Some(v)
      | (k, v) :: tail -> search tail
    search lst