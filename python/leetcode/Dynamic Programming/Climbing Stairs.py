class Solution:

    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        result = 0
        s1 = 1
        s2 = 2

        for i in range(2, n):
            result = s1 + s2
            s1 = s2
            s2 = result

        return result
