class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        postfix_product = 1
        for i in reversed(range(len(nums))):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result
