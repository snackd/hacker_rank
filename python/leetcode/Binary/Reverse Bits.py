class Solution:

    # def reverseBits(self, n: int) -> int:
    #     result = 0

    #     for i in range(32):

    #         # 3 = 11; check right 1
    #         if n & 1:

    #             result += pow(2, 31 - i)
    #         n = n >> 1

    #     return result

    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = (32 - len(n)) * "0" + n
        return int(n[::-1], 2)
