class Solution:

    # def maxProduct(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     result = nums[0]

    #     for i in range(len(nums)):
    #         current = 1
    #         for j in range(len(nums)):
    #             if (i == j):
    #                 current = nums[i]
    #             else:
    #                 current *= nums[j]

    #             result = max(result, current)

    #     return result

    # def maxProduct(self, nums: List[int]) -> int:

    #     if not nums:
    #         return 0

    #     # dynamic programming
    #     dp_max = [0] * len(nums)
    #     dp_min = [0] * len(nums)

    #     dp_max[0] = nums[0]
    #     dp_min[0] = nums[0]

    #     for i in range(1, len(nums)):
    #         if nums[i] > 0:
    #             dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
    #             dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])
    #         else:
    #             dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
    #             dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])

    #     return max(dp_max)

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for num in nums[1:]:
            temp = cur_max

            # cur_min * num = negative * negative = positive
            cur_max = max(cur_max * num, cur_min * num, num)

            # cur_max(temp) * num = positive * negative = negative
            cur_min = min(temp * num, cur_min * num, num)

            result = max(result, cur_max)

        return result
