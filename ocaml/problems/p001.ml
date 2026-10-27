open Core

let is_multiple n = n mod 3 = 0 || n mod 5 = 0

let () =
  let answer =
    List.range 1 1000 |> List.filter ~f:is_multiple |> List.fold ~init:0 ~f:( + )
  in
  assert (answer = 233168);
  printf "%d\n" answer
;;
