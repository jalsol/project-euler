# I try to solve Project Euler

Every problem gets its own executable in each language.

## C++ (Bazel)

    cd cpp
    bazel run //problems:p001

C++26, `-O3`, `-march=native` and friends come from `cpp/.bazelrc`, and builds
default to opt. Use `bazel run -c dbg` when you want asserts and debug info.
Drop `problems/pNNN.cpp` in; `problems/BUILD.bazel` globs `*.cpp` and creates one
`cc_binary` per file, named after it.

## OCaml (Dune)

    cd ocaml
    dune exec problems/p001.exe

Add `problems/pNNN.ml` and append its name to `(names ...)` in `problems/dune`.
