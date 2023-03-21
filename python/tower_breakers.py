#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    # Write your code here
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1
    """
    # 勝利條件:還可以移動
    # P1 已無法移動
    if m == 1:
        print(2)
    else:
        # n 可以被 2 整除的話，輪到 P1 時將無法移動
        if n % 2 == 1:
            print(1)
        else:
            print(2)
    """


if __name__ == '__main__':
    fold_path = os.path.abspath(os.getcwd())
    file_name = os.path.basename(__file__)[:-3] + '.txt'
    abs_path = fold_path + "\\" + file_name
    os.environ['OUTPUT_PATH'] = abs_path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
