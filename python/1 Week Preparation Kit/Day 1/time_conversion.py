#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    time = s.split(":")

    # 如果是 PM + 12 小時
    if s[-2:] == "PM":
        if int(time[0]) < 12:
            time[0] = str(int(time[0]) + 12)
    else:
        if int(time[0]) == 12:
            time[0] = "00"

    ntime = ':'.join(time)

    # print(ntime)

    # 去除 AM/PM
    return ntime[:-2]


if __name__ == '__main__':
    os.environ[
        'OUTPUT_PATH'] = "C:/Users/莊得仲/Desktop/hack_ranker/python/time_conversion/time_conversion.txt"

    # print("Modified OUTPUT_PATH:", os.environ['OUTPUT_PATH'])

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result)

    fptr.close()
