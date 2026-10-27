let is_multiple n = n mod 3 = 0 || n mod 5 = 0

let () =
  let answer =
    List.fold_left ( + ) 0 (List.filter is_multiple (List.init 999 (fun i -> i + 1)))
  in
  assert (answer = 233168);
  Printf.printf "%d\n" answer
