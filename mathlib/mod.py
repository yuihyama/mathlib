#!/usr/bin/env python

"""mod
"""

from numpy import mod as np_mod


def mod(x, y):
    """mod

    >>> mod([1, 2, 3.0, 4.0, 5], 2)
    array([1., 0., 1., 0., 1.])
    """
    return np_mod(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
