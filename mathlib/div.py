#!/usr/bin/env python

"""div
"""

from numpy import divide


def div(x, y):
    """div

    >>> div(4, 2)
    2.0
    >>> div([1, 2, 3], [4, 5.0, 6])
    array([0.25, 0.4 , 0.5 ])
    """
    return divide(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
