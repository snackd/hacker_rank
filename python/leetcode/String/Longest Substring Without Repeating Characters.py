class Solution:

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0

    #     result = 0
    #     left = 0
    #     temp_list = []

    #     for right in range(len(s)):
    #         while s[right] in temp_list:
    #             temp_list.pop(0)
    #             left += 1
    #         temp_list.append(s[r])
    #         result = max(result, right - left + 1)

    #     return result

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        result = 0
        left = 0

        # right (pointer):0, 1, 2, 3
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result
