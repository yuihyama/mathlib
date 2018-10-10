#!/usr/bin/env python

"""sub
"""

from numpy import subtract


def sub(x, y):
    """sub
    >>> sub(2, 1)
    1
    >>> sub([1, 2, 3], [1, 2, 3])
    array([0, 0, 0])
    """
    return subtract(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
