class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = True

        return False
        # return len(nums) != len(set(nums))
