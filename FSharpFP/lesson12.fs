// 34.1
let upto n =
  let rec _upto = function
    | (iter, arr) when iter > n -> arr
    | (iter, arr) -> iter :: _upto(iter + 1, arr)
  _upto(1, [])

// 34.2
let dnto n = 
  let rec _dnto = function
    | (iter, arr) when iter <= 0 -> arr
    | (iter, arr) -> iter :: _dnto(iter - 1, arr)
  _dnto(n, [])

// 34.3
let evenn n = 
  let rec _evenn = function
    | (iter, len, arr) when len >= n -> arr
    | (iter, len, arr) when iter % 2 = 0 -> iter :: _evenn(iter + 1, len + 1, arr)
    | (iter, len, arr)-> _evenn(iter + 1, len, arr)
  _evenn(0, 0, [])