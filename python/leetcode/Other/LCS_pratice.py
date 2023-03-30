def LCS(str1, str2):
    if not str1 or not str2:
        return 0

    # dp = [[0] * (len(str2) + 1)] * (len(str1) + 1)
    # prev = dp.copy()
    # prev = [[0] * (len(str2) + 1)] * (len(str1) + 1)

    dp = []
    for i in range(len(str1) + 1):
        row = []
        for j in range(len(str2) + 1):
            value = 0
            row.append(value)
        dp.append(row)

    prev = []
    for i in range(len(str1) + 1):
        row = []
        for j in range(len(str2) + 1):
            value = 0
            row.append(value)
        prev.append(row)

    for i in range(1, len(str1) + 1):

        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # 左上
                prev[i][j] = 0
            else:
                # 左 < 上
                if dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                    # 左
                    prev[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
                    # 上
                    prev[i][j] = 2
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print(len(prev))
    # print(len(prev[0]))

    # lcs = ""

    # # Start from the right-most-bottom-most corner and
    # # one by one store characters in lcs[]
    # i = len(str1)
    # j = len(str2)
    # while i > 0 and j > 0:
    #     # If current character in X[] and Y are same, then
    #     # current character is part of LCS
    #     if str1[i - 1] == str2[j - 1]:
    #         print(i, j)
    #         lcs += str1[i - 1]
    #         i -= 1
    #         j -= 1
    #     # If not same, then find the larger of two and
    #     # go in the direction of larger value
    #     elif dp[i - 1][j] < dp[i][j - 1]:
    #         j -= 1
    #     else:
    #         i -= 1

    # lcs = lcs[::-1]
    # print("LCS of " + str1 + " and " + str2 + " is " + lcs)
    lcs = [0, 0, 0, 0, 0]

    def LCS_loop(i, j):
        length = dp[i][j]
        while length > 0:
            if (prev[i][j] == 0):
                length -= 1
                lcs[length] = str1[i - 1]
                i -= 1
                j -= 1
            elif prev[i][j] == 1:
                j -= 1
            elif prev[i][j] == 2:
                i -= 1
            # if str1[i - 1] == str2[j - 1]:
            #     length -= 1
            #     lcs[length] = str1[i - 1]
            # elif dp[i - 1][j] < dp[i][j - 1]:
            #     j -= 1
            # else:
            #     i -= 1

        length = dp[i][j]
        for i in range(length):
            print(lcs[i], end="")
        print()
        print(lcs)

    LCS_loop(len(str1), len(str2))

    # Recursive
    # def LCS_recursive(i, j):
    #     if i == 0 or j == 0:
    #         return 0

    #     if prev[i][j] == 0:
    #         LCS_recursive(i - 1, j - 1)
    #         print(str1[i - 1], end="")
    #     elif prev[i][j] == 1:
    #         LCS_recursive(i, j - 1)
    #     else:
    #         LCS_recursive(i - 1, j)

    # LCS_recursive(len(str1), len(str2))

    return dp[-1][-1]


s1 = "abcde"
s2 = "cbda"
# s1 = [0, 2, 5, 7, 9, 3, 1, 2]
# s2 = [0, 3, 5, 3, 2, 8]
print(LCS(s1, s2))
