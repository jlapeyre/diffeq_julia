import DiffEqBase
import PyCall

PyCall.PyObject(::typeof(DiffEqBase.solve)) =
    PyCall.pyfunctionret(DiffEqBase.solve,Any,Vararg{PyCall.PyAny})

function DiffEqBase.numargs(f::PyCall.PyObject)
    inspect = PyCall.pyimport("inspect")
    PyCall.hasproperty(f,:py_func) ? _f = f.py_func : _f = f
    nargs = length(first(inspect.getfullargspec(_f)))
    if inspect.ismethod(_f)
        # `f` is a bound method (i.e., `self.f`) but `getfullargspec`
        # includes `self` in the `args` list.  So, we are subtracting
        # 1 manually here:
        return nargs - 1
    else
        return nargs
    end
end
