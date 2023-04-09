class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1

        return count
