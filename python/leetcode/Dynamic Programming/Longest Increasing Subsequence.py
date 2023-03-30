class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # set element len from 1 (subsequence)
        # Space = O(N)
        dp = [1] * len(nums)
        dp[0] = 1

        # Time: (N^2)
        for i in range(1, len(nums)):
            for j in range(0, i):
                # element len + 1
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
