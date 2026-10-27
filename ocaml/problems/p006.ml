open Core

let () =
  let n = 100 in
  let range = List.init (n + 1) ~f:Fn.id in
  let square x = x * x in
  let sum = List.fold ~init:0 ~f:Int.( + ) in
  let sum_of_squares = range |> List.map ~f:square |> sum in
  let square_of_sums = range |> sum |> square in
  printf "%d\n" (abs (sum_of_squares - square_of_sums))
;;
