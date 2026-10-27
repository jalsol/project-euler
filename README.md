# I try to solve Project Euler

im stupid at math but can i abuse computational power?

## Running

    ./run 6          # every language that has problem 6
    ./run cpp 6
    ./run ocaml 6
    ./run python 6

`./run` syncs OCaml's static `(names ...)` list from `problems/*.ml` before
building, since dune has no glob for executable names.

## Creating a problem

    ./new cpp 7
    ./new ocaml 7
    ./new python 7

Writes an empty `problems/pNNN.<ext>` and refuses to overwrite.

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

Add `problems/pNNN.ml`; `./run` picks up its name. Jane Street Core is linked in
via `(libraries core)`.

## Python (uv)

    cd python
    uv run problems/p001.py

Drop `problems/pNNN.py` in; `./run python N` runs it with uv. Requires Python
3.14+, per `pyproject.toml`; add dependencies with `uv add`.
