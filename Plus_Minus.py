#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *

# Complete the plusMinus function below.


def plusMinus(arr):
    pos = []
    neg = []
    zer = []
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        elif i == 0:
            zer.append(i)
    context = Context(prec=6)
    getcontext().prec = 6
    totpos = len(pos)/n
    totneg = len(neg)/n
    totzer = len(zer)/n
    return format(totpos, ".6f"), format(totneg, ".6f"), format(totzer, ".6f")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    cool = plusMinus(arr)
    print(cool)
    # print('/n'.join(plusMinus))
