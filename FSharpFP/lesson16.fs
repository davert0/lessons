// 42.3
let rec allSubsets n k =
  let rec subsets = function
    | [] -> [[]]
    | head::tail -> List.foldBack (fun cur acc -> if List.length cur < k then (head::cur)::cur::acc else cur::acc) (subsets tail) []

  let res = subsets [1..n]
  let filtered = List.filter (fun l -> List.length l = k) res
  Set.ofList (List.map (fun l -> Set.ofList l) filtered)