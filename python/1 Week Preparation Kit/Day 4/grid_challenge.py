#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    # grid = [70, 80, 75, 65, 88, 73, 76, 77, 82]
    # grid = [chr(e) for e in grid]

    # grid = ['abc', 'qwe', 'zxc']

    grid = [list(row) for row in grid]

    r = len(grid)
    c = len(grid[0])

    # 依照 grid[i] 依序將英文字母排列
    for i in range(r):
        grid[i].sort()

    for j in range(c):
        for i in range(1, r):

            # 如果非下一列頭個字母大於上列，那麼就無按照大小排序
            if not grid[i - 1][j] <= grid[i][j]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    fold_path = os.path.abspath(os.getcwd())
    file_name = os.path.basename(__file__)[:-3] + '.txt'
    abs_path = fold_path + "\\" + file_name
    os.environ['OUTPUT_PATH'] = abs_path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
