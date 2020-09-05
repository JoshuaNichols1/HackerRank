#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    final = []
    for i in grades:
        i2 = i
        if i < 38:
            final.append(str(i))
        else:
            if i//5 != i/5:
                i2 = ((i//5)*5)+5
            if (i2 - i) < 3:
                i = i2
            final.append(str(i))
    return final


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print('\n'.join(result))

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
