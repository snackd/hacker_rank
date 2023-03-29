class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     if not height:
    #         return 0

    #     contain = 0

    #     for left in range(len(height)):
    #         second_height = 0
    #         for right in range(len(height)-1, 0, -1):
    #             if second_height >= min(height[left], height[right]):
    #                 continue
    #             else:
    #                 second_height = min(height[left], height[right])
    #                 contain = max(contain, (right-left)*second_height)

    #     return contain

    def maxArea(self, height: List[int]) -> int:

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        contain = 0

        while left < right:
            if height[left] <= height[right]:
                contain = max(height[left] * (right - left), contain)
                left += 1
            else:
                contain = max(height[right] * (right - left), contain)
                right -= 1

        return contain
