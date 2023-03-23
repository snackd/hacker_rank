#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heapify, heappush, heappop
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here
    heapify(A)
    result = 0

    # main logic
    while True:
        x = heappop(A)

        # base condition
        if x >= k:
            return result
        if A:
            y = heappop(A)
            s = x + 2 * y
            heappush(A, s)
            result += 1
        else:
            return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
