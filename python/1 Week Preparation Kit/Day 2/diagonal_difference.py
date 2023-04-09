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
    # Write your code here
    # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    first_sum = 0
    second_sum = 0

    length = len(arr[0])
    for i in range(length):
        # X * *
        # * X *
        # * * X
        first_sum += arr[i][i]
        # * * X
        # * X *
        # X * *
        second_sum += arr[i][(length - i - 1)]

    return abs(first_sum - second_sum)


if __name__ == '__main__':
    fold_path = os.path.abspath(os.getcwd())
    file_name = os.path.basename(__file__)[:-3] + '.txt'
    abs_path = fold_path + "\\" + file_name
    os.environ['OUTPUT_PATH'] = abs_path

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
