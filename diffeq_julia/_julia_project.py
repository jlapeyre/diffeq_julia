import julia
import logging

from julia_project import JuliaProject

import os
diffeq_julia_path = os.path.dirname(os.path.abspath(__file__))

julia_project = JuliaProject(
    name="diffeq_julia",
    package_path=diffeq_julia_path,
    preferred_julia_versions = ['1.7', '1.6', 'latest'],
    env_prefix = 'DIFFEQ_JULIA_',
    logging_level = logging.INFO, # or logging.WARN,
    console_logging=False
)

julia_project.run()

# logger = julia_project.logger

def compile_diffeq_julia():
    """
    Compile a system image for `diffeq_julia` in the subdirectory `./sys_image/`. This
    system image will be loaded the next time you import `diffeq_julia`.
    """
    julia_project.compile_julia_project()


def update_diffeq_julia():
    """
    Remove possible stale Manifest.toml files and compiled system image.
    Update Julia packages and rebuild Manifest.toml file.
    Before compiling, it's probably a good idea to call this method, then restart Python.
    """
    julia_project.update()


