type F = 
  | AM
  | PM
type TimeOfDay = { hours: int; minutes: int; f: F }

let transform (x: TimeOfDay) = 
    let hours = function
      | AM -> 0
      | PM -> 12
      | _ -> 0
    (x.hours + hours x.f) * 60 + x.minutes

let (.>.) x y = (transform x) > (transform y)