#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pairs(k, arr):
    # Write your code here
    # k = 1
    # arr = [1, 5, 3, 4, 2]
    d = Counter(arr)
    pairs = 0

    for i in arr:
        if i + k in d:
            pairs += 1
        if i - k in d:
            pairs += 1
        del d[i]
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
