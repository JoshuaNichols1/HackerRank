#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#


def simpleArraySum(ar):
    k = 0
    for i in ar:
        k += i
    return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
