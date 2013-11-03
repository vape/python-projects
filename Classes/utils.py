from functools import wraps
from inspect import getargspec


def initializer(private=False):
    """
    Stolen from [http://stackoverflow.com/a/1389216/36938]
    Decorator used to avoid property initialization boilerplate
    in class __init__ methods.
    i.e. for SomeClass with constructor __init__(self, a, b, c)
    instead of writing
    self._a = a
    self._b = b etc, you just decorate the constructor with @initializer.
    @param private: Boolean parameter which specifies whether the auto-generated fields should be
    named in the private naming convention (e.g. _name, _id) or the
    actual parameter names should be used for field names.
    Default value is False
    """
    def initialize(fun):
        names, varargs, keywords, defaults = getargspec(fun)
        @wraps(fun)
        def wrapper(self, *args):
            for name, arg in zip(names[1:], args + (defaults or ())):
                setattr(self, '{0}{1}'.format('_' if private else '', name), arg)
            fun(self, *args)
        return wrapper
    return initialize
