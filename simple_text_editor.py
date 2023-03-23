# -*- coding: utf-8 -*-

# 設置
stack = []
string = ""

for _ in range(int(input())):
    t = input().split()
    # check for query type
    # append the string
    if t[0] == '1':
        stack.append(string)
        string += t[1]

    # delete the string
    elif t[0] == '2':
        stack.append(string)
        string = string[:-int(t[1])]

    # print char of a string
    elif t[0] == '3':
        print(string[int(t[1]) - 1])

    # undo operation
    else:
        string = stack.pop()
