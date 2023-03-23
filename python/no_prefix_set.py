#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


def insert(trie, word):
    for i, char in enumerate(word):
        if char in trie:
            if trie[char][1] or i == len(word) - 1:
                return True
        else:
            trie[char] = {}, i == len(word) - 1

        trie, _ = trie[char]

    return False


def noPrefix(words):
    # Write your code here
    trie = {}
    for word in words:
        if insert(trie, word):
            print("BAD SET")
            print(word)
            return

    print("GOOD SET")


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
