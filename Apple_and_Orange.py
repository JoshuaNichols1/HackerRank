#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    final1 = 0
    final2 = 0
    for i in apples:
        if s <= (a + i) <= t:
            final1 += 1
    for i in oranges:
        if s <= (b+i) <= t:
            final2 += 1
    return str(final1), str(final2)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    cool = countApplesAndOranges(s, t, a, b, apples, oranges)
    print('\n'.join(cool))
