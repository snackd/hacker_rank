#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def shiftAlphabet(c, k):
    # uppercase: 65-90
    if 65 <= c <= 90:
        c += k
        if c < 65:
            c += 26
        elif c > 90:
            c -= 26

    # lowercase: 97-122
    elif 97 <= c <= 122:
        c += k
        if c < 97:
            c += 26
        elif c > 122:
            c -= 26

    return chr(c)


def caesarCipher(s, k):
    # Write your code here
    temp_list = []
    k %= 26
    for i in s:
        temp_list.append(shiftAlphabet(ord(i), k))

    return ''.join(temp_list)


if __name__ == '__main__':
    fold_path = os.path.abspath(os.getcwd())
    file_name = os.path.basename(__file__)[:-3] + '.txt'
    abs_path = fold_path + "\\" + file_name
    os.environ['OUTPUT_PATH'] = abs_path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
