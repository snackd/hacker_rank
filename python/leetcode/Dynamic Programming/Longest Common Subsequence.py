class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        dp = []
        count = 0
        for i in range(len(text1) + 1):
            rows = []
            for j in range(len(text2) + 1):
                rows.append(count)
            dp.append(rows)

        # LCS
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 取左上格 element 再 + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 如果上方大於左方
                    if dp[i - 1][j] < dp[i][j - 1]:
                        # 此格 = 上方值
                        dp[i][j] = dp[i][j - 1]
                    else:
                        # 此格 = 左方值
                        dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]
