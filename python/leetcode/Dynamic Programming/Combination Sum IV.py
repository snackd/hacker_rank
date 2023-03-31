class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        nums.sort()

        dp = [0] * (target +1 )
        for i in range(1, target+1):
            for num in nums:
                if i == num:
                    dp[i] += 1
                if i - num >= 0:
                    dp[i] += dp[i-num]

        return dp[-1]
