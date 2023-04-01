class Solution:

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     if not matrix:
    #         return None

    #     left, right = 0, len(matrix) - 1

    # while left < right:
    #     for i in range(right - left):
    #         top, bottom = left, right

    #         top_left = matrix[top][left + i]

    #         matrix[top][left + i] = matrix[bottom - i][left]

    #         matrix[bottom - i][left] = matrix[bottom][right - i]

    #         matrix[bottom][right - i] = matrix[top + i][right]

    #         matrix[top + i][right] = top_left

    #     right -= 1
    #     left += 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None

        # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],
        #           [15, 14, 12, 16]]

        # matrix = [[n + i for i in range(4)] for n in range(1, 4 * 4 + 1, 4)]

        row = len(matrix)
        col = len(matrix[0])

        if row != col:
            return None

        # matrix.reverse()
        # [0][0], [-1][0] = [-1][0], [0][0]
        for i in range(row // 2):
            for j in range(col):
                matrix[i][j], matrix[row - i -
                                     1][j] = matrix[row - i -
                                                    1][j], matrix[i][j]
        # [1][0], [0][1] = [1][0], [0][1]
        # [2][0], [0][2]
        # [2][1], [1][2]
        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
