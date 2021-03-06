# diffeq_julia

An alternative packaging for [diffeqpy](https://github.com/SciML/diffeqpy) using [`julia_project`](https://github.com/jlapeyre/julia_project).
This manages: installing Julia, installing Julia packages, building and loading a system image.

* Install this python package.
    * Clone or otherwise download this package.
    * Do `pip install /path/to/download`. Or change to this path and do `pip install .`.

* In python, do `import diffeq_julia`

* `diffeq_julia.compile_diffeq_julia()` compiles a system image. You will also be offered to compile the first time you import.

* `diffeq_julia.update_diffeq_julia()` deletes the system image and updates the Julia packages


### Use

All of the examples in the README in [diffeqpy](https://github.com/SciML/diffeqpy) should work as written,
except that `diffeqpy` must be replaced by `diffeq_julia`. This is done just to avoid confusion.
If you don't have both packages installed, you could do `import diffeq_julia as diffeqpy`.

