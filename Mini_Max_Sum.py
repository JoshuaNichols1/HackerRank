#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    final = []
    Sum = sum(arr)
    for i in range(len(arr)):
        if s1 == 0:
            s1 = Sum - arr[0]
            final.append(str(s1))
        elif s2 == 0:
            s2 = Sum - arr[1]
            final.append(str(s2))
        elif s3 == 0:
            s3 = Sum - arr[2]
            final.append(str(s3))
        elif s4 == 0:
            s4 = Sum - arr[3]
            final.append(str(s4))
        elif s5 == 0:
            s5 = Sum - arr[4]
            final.append(str(s5))
    return min(final), max(final)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    cool = miniMaxSum(arr)
    print(' '.join(cool))
