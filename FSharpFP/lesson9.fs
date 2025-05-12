let formatG x = 
  let (x_g, x_s, x_m) = x
  let (n_s_1, n_m) = (x_m / 12, x_m % 12)
  let (n_g, n_s_2) = ((n_s_1 + x_s) / 20, (n_s_1 + x_s) % 20)
  (x_g + n_g, n_s_2, n_m)
  
// 23.4.1
let (.+.) x y =
  let (x_g, x_s, x_m) = x
  let (y_g, y_s, y_m) = y
  formatG(x_g + y_g, x_s + y_s, x_m + y_m)

let (.-.) x y =
  let (x_g, x_s, x_m) = x
  let (y_g, y_s, y_m) = y
  formatG(x_g - y_g, x_s - y_s, x_m - y_m)

// 23.4.2
let (.+) x y = 
  let (a, b) = x
  let (c, d) = y
  (a + c, b + d)

let (.-) x y =
  let (a, b) = y
  x .+ (-a, -b)

let (.*) x y =
  let (a, b) = x
  let (c, d) = y
  (a*c - b*d, b*c + a*d)

let (./) x y =
  let (a, b) = y
  x .* (a/(a*a+b*b), -b/(a*a+b*b))