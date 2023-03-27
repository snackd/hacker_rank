class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        # float('inf') represent unprocessed, infinities
        dp = [float('inf')] * (amount + 1)

        # min_coins solution
        dp[0] = 0

        # example:
        # dp[1] = 1
        # dp[2] = 2; 2 times 1 coins, (0+1) = 1 times 2 coins
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # if dp[-1] == float('inf'), No solution
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
