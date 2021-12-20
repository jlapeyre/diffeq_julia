# diffeq_julia

An alternative packaging for [diffeqpy](https://github.com/SciML/diffeqpy) using [`julia_project`](https://github.com/jlapeyre/julia_project).
This manages, installing Julia, installing Julia packages, building and loading a system image.

* Install this python package.

* In python, do `import diffeq_julia`

* `diffeq_julia.compile_diffeq_julia()` compiles a system image

* `diffeq_julia.update_diffeq_julia()` deletes the system image and updates the Julia packages

