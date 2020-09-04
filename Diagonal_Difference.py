#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(n-1):
        cool = arr[0] + arr[(i+1) + n]
        d1 += cool
        print(d1)
    for ii in range(n-1):
        ii = n-1
        cool2 = arr[n-1] + arr[ii + n]
        d2 += cool2
        print(d2)
    if d1 > d2:
        return d1-d2
    else:
        return d2 - d1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('dd.txt', 'r')
    n = int(input().strip())

    arr = []

    for line in fptr.read().split():
        line = int(line)
        arr.append(line)

    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
