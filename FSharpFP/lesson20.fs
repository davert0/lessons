// 49.5.1
let even_seq = Seq.initInfinite (fun i -> 2 * (i + 1))

// 49.5.2
let fac_seq = 
    let fact n = 
      let rec _fact v acc = 
        match v with
          | 0 -> acc
          | 1 -> acc
          | _ -> _fact (v - 1) (acc * v)
      _fact n 1
    Seq.initInfinite fact


// 49.5.3
let seq_seq = Seq.initInfinite (fun i -> if i % 2 = 0 then i / 2 else -(i+1)/2)