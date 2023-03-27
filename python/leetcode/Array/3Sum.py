class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Preventation
        if len(nums) <= 2: return []

        # Sort
        nums.sort()

        # Init
        results = []
        target = 0

        # Find the match ans
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left = i + 1
            right = len(nums) - 1

            while (left < right):
                if (left > i + 1 and right < len(nums) - 1):
                    if nums[left] == nums[left -
                                          1] and nums[right] == nums[right +
                                                                     1]:
                        left += 1
                        right -= 1
                        continue

                sum_result = nums[i] + nums[left] + nums[right]

                if sum_result == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum_result < 0:
                    left += 1
                elif sum_result > 0:
                    right -= 1

        return results
