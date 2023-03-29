class Solution:

    # def findMin(self, nums: List[int]) -> int:
    #     result = nums[0]
    #     left = 0
    #     right = len(nums) - 1

    #     while left < right:
    #         if nums[left] < nums[right]:
    #             result = min(result, nums[left])
    #             break

    #         mid = (left + right) // 2
    #         result = min(result, nums[mid])
    #         if nums[mid] >= nums[left]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return result

    # def findMin(self, nums: List[int]) -> int:
    #     min_value = nums[0]
    #     for i in range(len(nums)):
    #         if nums[i] < min_value:
    #             min_value = nums[i]

    #     return min_value

    def findMin(self, nums: List[int]) -> int:
        return min(nums)
