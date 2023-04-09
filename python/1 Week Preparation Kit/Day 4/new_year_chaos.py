#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    # q = [1, 2, 3, 4, 5]
    # q = [5, 4, 3, 2, 1]
    bribes = 0

    # set queue to start at 0
    q = [i - 1 for i in q]

    for index, element in enumerate(q):
        current = index
        if element - current > 2:
            print("Too chaotic")
            # return

        for k in q[max(element - 1, 0):index]:
            print(k)
            if k > element:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
