class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
            result = max(result, nums[i])

        return result
