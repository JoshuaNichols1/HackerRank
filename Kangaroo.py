#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and v2 != v1:
        print('NO')
    elif (v1 - v2) > 1 or (v2-v1) > 1:
        print('NO')
    else:
        if x2 > x1 and v2 > v1:
            print('NO')
        elif x1 > x2 and v1 > v2:
            print('NO')
        elif x2 > x1 and v1 > v2:
            print('YES')
        elif x1 > x2 and v2 > v1:
            print('YES')
        # r1 = x1 + v1
        # r2 = x2 + v2
        # while r1 != r2:
        #     r1 += x1 + v1
        #     r2 += x2 + v2
        # else:
        #     print('YES')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    # fptr.write(result + '\n')

    # fptr.close()
