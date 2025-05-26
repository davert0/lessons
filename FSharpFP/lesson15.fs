// 41.4.1
let list_filter f xs = List.foldBack (fun lst cur -> if f lst then lst::cur else cur) xs []

// 41.4.2
let sum (p, xs) = List.foldBack (fun cur vl -> if p cur then cur + vl else vl) xs 0

// 41.4.3
let revrev lst = List.fold (fun head tail -> (List.rev tail)::head) [] lst