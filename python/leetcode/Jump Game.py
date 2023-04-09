class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        max_i = 0
        for i, num in enumerate(nums):
            if i > max_i:
                return False
            max_i = max(num + i, max_i)

        return max_i >= len(nums) - 1
