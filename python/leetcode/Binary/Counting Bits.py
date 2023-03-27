class Solution:

    # def countBits(self, n: int) -> List[int]:

    #     results = [0]

    #     for i in range(1, n + 1):
    #         count_1 = 0

    #         while i > 0:
    #             if i % 2 != 0:
    #                 count_1 += 1
    #             i = i // 2

    #         results.append(count_1)

    #     return results

    def countBits(self, n: int) -> List[int]:

        # Dynamic Programming
        if n == 0:
            return [0]

        results = [0] * (n + 1)
        results[1] = 1

        for i in range(2, n + 1):
            # Odd:3 = 011, result[1] + 1 = 2
            if i % 2 == 1:
                results[i] = results[i // 2] + 1

            # Even:2 = 10, 4 = 100, 6 = 110;results[3] = 2
            else:
                results[i] = results[i // 2]

        return results
