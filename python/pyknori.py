# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pyknori')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pyknori')
    _pyknori = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyknori', [dirname(__file__)])
        except ImportError:
            import _pyknori
            return _pyknori
        try:
            _mod = imp.load_module('_pyknori', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pyknori = swig_import_helper()
    del swig_import_helper
else:
    import _pyknori
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyknori.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pyknori.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pyknori.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pyknori.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pyknori.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pyknori.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pyknori.SwigPyIterator_copy(self)

    def next(self):
        return _pyknori.SwigPyIterator_next(self)

    def __next__(self):
        return _pyknori.SwigPyIterator___next__(self)

    def previous(self):
        return _pyknori.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pyknori.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pyknori.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pyknori.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pyknori.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pyknori.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pyknori.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pyknori.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pyknori.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

INIT = _pyknori.INIT
ESTEP = _pyknori.ESTEP
EUCL = _pyknori.EUCL
COS = _pyknori.COS
RANDOM = _pyknori.RANDOM
FORGY = _pyknori.FORGY
PLUSPLUS = _pyknori.PLUSPLUS
NONE = _pyknori.NONE
class kmeans_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, kmeans_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, kmeans_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nrow"] = _pyknori.kmeans_t_nrow_set
    __swig_getmethods__["nrow"] = _pyknori.kmeans_t_nrow_get
    if _newclass:
        nrow = _swig_property(_pyknori.kmeans_t_nrow_get, _pyknori.kmeans_t_nrow_set)
    __swig_setmethods__["ncol"] = _pyknori.kmeans_t_ncol_set
    __swig_getmethods__["ncol"] = _pyknori.kmeans_t_ncol_get
    if _newclass:
        ncol = _swig_property(_pyknori.kmeans_t_ncol_get, _pyknori.kmeans_t_ncol_set)
    __swig_setmethods__["iters"] = _pyknori.kmeans_t_iters_set
    __swig_getmethods__["iters"] = _pyknori.kmeans_t_iters_get
    if _newclass:
        iters = _swig_property(_pyknori.kmeans_t_iters_get, _pyknori.kmeans_t_iters_set)
    __swig_setmethods__["k"] = _pyknori.kmeans_t_k_set
    __swig_getmethods__["k"] = _pyknori.kmeans_t_k_get
    if _newclass:
        k = _swig_property(_pyknori.kmeans_t_k_get, _pyknori.kmeans_t_k_set)
    __swig_setmethods__["assignments"] = _pyknori.kmeans_t_assignments_set
    __swig_getmethods__["assignments"] = _pyknori.kmeans_t_assignments_get
    if _newclass:
        assignments = _swig_property(_pyknori.kmeans_t_assignments_get, _pyknori.kmeans_t_assignments_set)
    __swig_setmethods__["assignment_count"] = _pyknori.kmeans_t_assignment_count_set
    __swig_getmethods__["assignment_count"] = _pyknori.kmeans_t_assignment_count_get
    if _newclass:
        assignment_count = _swig_property(_pyknori.kmeans_t_assignment_count_get, _pyknori.kmeans_t_assignment_count_set)
    __swig_setmethods__["centroids"] = _pyknori.kmeans_t_centroids_set
    __swig_getmethods__["centroids"] = _pyknori.kmeans_t_centroids_get
    if _newclass:
        centroids = _swig_property(_pyknori.kmeans_t_centroids_get, _pyknori.kmeans_t_centroids_set)

    def __init__(self, *args):
        this = _pyknori.new_kmeans_t(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def _print(self):
        return _pyknori.kmeans_t__print(self)

    def write(self, dirname):
        return _pyknori.kmeans_t_write(self, dirname)

    def __eq__(self, other):
        return _pyknori.kmeans_t___eq__(self, other)

    def set_params(self, nrow, ncol, iters, k):
        return _pyknori.kmeans_t_set_params(self, nrow, ncol, iters, k)

    def set_computed(self, assignments_buf, assignment_count_buf, centroids):
        return _pyknori.kmeans_t_set_computed(self, assignments_buf, assignment_count_buf, centroids)
    __swig_destroy__ = _pyknori.delete_kmeans_t
    __del__ = lambda self: None
kmeans_t_swigregister = _pyknori.kmeans_t_swigregister
kmeans_t_swigregister(kmeans_t)
cvar = _pyknori.cvar
INVALID_CLUSTER_ID = cvar.INVALID_CLUSTER_ID


def kmeans(*args):
    return _pyknori.kmeans(*args)
kmeans = _pyknori.kmeans
# This file is compatible with both classic and new-style classes.


