#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    appear_time_list = [0 for i in range(100)]
    for num in arr:
        appear_time_list[num] += 1

    return appear_time_list


def test_countingSort(arr):
    # arr = [0] * 100
    # arr = []
    # for i in range(10):
    #     arr.append(random.randint(1, 10))

    # 0-100
    appear_time_list = [0 for i in range(len(arr) + 1)]
    for num in arr:
        appear_time_list[num] += 1

    # print(appear_time_list)

    # 0-99
    return appear_time_list[:-1]


if __name__ == '__main__':
    fold_path = os.path.abspath(os.getcwd())
    file_name = os.path.basename(__file__)[:-3] + '.txt'
    abs_path = fold_path + "\\" + file_name
    os.environ['OUTPUT_PATH'] = abs_path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
