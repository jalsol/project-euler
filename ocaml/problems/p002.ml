open Core

let () =
  let ans =
    Sequence.unfold ~init:(1, 2) ~f:(fun (a, b) -> Some (a, (b, a + b)))
    |> Sequence.take_while ~f:(Int.( >= ) 4_000_000)
    |> Sequence.filter ~f:(fun x -> x % 2 = 0)
    |> Sequence.fold ~init:0 ~f:Int.( + )
  in
  printf "%d\n" ans
;;
