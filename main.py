#!/usr/bin/env python

"""main
"""

from mathlib.add import add
from mathlib.sub import sub


if __name__ == '__main__':
    # add()
    print(add(1, 2))
    print(add([1, 2, 3], [1, 2, 3]))

    # sub()
    print(sub(2, 1))
    print(sub([1, 2, 3], [1, 2, 3]))

    # add(), sub()
    for i, j in zip([1, 2, 3], [1, 2, 3]):
        print('add(i, j):')
        print(add(i, j))
        print('')
        print('sub(add(i, j), i):')
        print(sub(add(i, j), i))
        print('')
