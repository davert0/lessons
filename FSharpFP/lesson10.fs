type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y = 
    let toMinutes t = 
        let baseHours = if t.f = "AM" then 0 else 12
        (baseHours + t.hours) * 60 + t.minutes
    let minutesX = toMinutes x
    let minutesY = toMinutes y
    minutesX > minutesY
