from setuptools import setup

version = {}
with open("./diffeq_julia/_version.py") as fp:
    exec(fp.read(), version)

setup(
    name='diffeq_julia',
    version=version['__version__'],
    description='Solving Differential Equations in Python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords='differential equations stochastic ordinary delay differential-algebraic dae ode sde dde',
    author='John Lapeyre',
    license='MIT',
    packages=['diffeq_julia'],
    install_requires=['julia>=0.2'],
    include_package_data=True,
    zip_safe=False)
