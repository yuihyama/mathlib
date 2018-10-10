#!/usr/bin/env python

"""add
"""

from numpy import add as np_add


def add(x, y):
    """add

    >>> add(1, 2)
    3
    >>> add([1, 2, 3], [1, 2, 3])
    array([2, 4, 6])
    """
    return np_add(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
