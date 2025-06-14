// 50.2.1
let fac_seq = 
    let fact n = 
      let rec _fact v acc = 
        match v with
          | 0 -> acc
          | 1 -> acc
          | _ -> _fact (v - 1) (acc * v)
      _fact n 1
    let rec fibs n = seq { yield fact n; yield! fibs (n+1) }
    fibs 0

// 50.2.2
let seq_seq = 
    let rec sq n = seq { 
      if n % 2 = 0 then yield n/2 
      else yield (-1) * (n + 1) / 2
      yield! sq (n+1) 
    }
    sq 0