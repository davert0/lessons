// 47.4.1
let f n: int = 
  if n = 0 then 1
  else 
    let mutable fact = 1
    let inn x = fact <- fact * x
    List.iter inn [1..n]
    fact

// 47.4.2
let fibo n = 
  if n = 0 then 0
  else 
    let mutable last = 0
    let mutable next = 1

    let iter x = 
      let temp = last + next
      last <- next
      next <- temp

    List.iter iter [1..n-1]
    next