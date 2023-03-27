class Solution:

    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     sum_n = sum(nums)

    #     # 1+2+...+100 = 5050, 1+100 * 100/2= 5050
    #     return int(n * (n + 1) / 2 - sum_n)

    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            # O(1)
            if i not in num_set:
                return i
