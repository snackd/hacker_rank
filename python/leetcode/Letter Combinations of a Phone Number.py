class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []

        def letterCombinationHelper(digits, slate):
            if len(digits) == 0:
                result.append(slate)
                return
            for letter in keypad[digits[0]]:
                letterCombinationHelper(digits[1:], slate + letter)

        if digits:
            letterCombinationHelper(digits, "")

        return result
