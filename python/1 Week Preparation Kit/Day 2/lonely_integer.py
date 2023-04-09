#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    result = [val for val in a if a.count(val) == 1]
    for i in result:
        return i


def test_lonelyinteger(a):
    for val in a:
        if a.count(val) == 1:
            result = val
            return result

    # input_data = [1, 2, "3"]
    # if (type(input_data[0]) is int):
    #     print(1)
    # else:
    #     print(0)
    # result = [val for val in input_data if type(val) is int]


if __name__ == '__main__':
    os.environ[
        'OUTPUT_PATH'] = "C:/Users/莊得仲/Desktop/hack_ranker/python/lonely_integer/lonely_integer.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
