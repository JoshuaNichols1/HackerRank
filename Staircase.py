#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.


def staircase(n):
    k = ''
    a = []
    for i in range(n):
        i = n-(i+1)
        k += '#'
        a.append((i*' ') + k)
    return a


if __name__ == '__main__':
    n = int(input())
    cool = staircase(n)
    print('\n'.join(cool))
