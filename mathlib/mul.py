#!/usr/bin/env python

"""mul
"""

from numpy import multiply


def mul(x, y):
    """mul

    >>> mul(2, 3)
    6
    >>> mul([1, 2, 3], [1, 2, 3])
    array([1, 4, 9])
    >>> mul([1.0, 2.0, 3.0], [4, 5, 6])
    array([ 4., 10., 18.])
    """
    return multiply(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
