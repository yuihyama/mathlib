#!/usr/bin/env python

"""numpy pow
"""

from numpy import power


def np_pow(x, y):
    """numpy pow

    >>> np_pow(2, 3)
    8
    >>> np_pow([1, 2, 3], [1, 2, 3])
    array([ 1,  4, 27])
    >>> np_pow([1.0, 2, 3.0], [1, 2.0, 3.0])
    array([ 1.,  4., 27.])
    """
    return power(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
