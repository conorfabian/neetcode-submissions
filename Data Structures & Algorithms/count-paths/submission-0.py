class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r - 1 >= 0:
                    grid[r][c] += grid[r - 1][c]
                if c - 1 >= 0:
                    grid[r][c] += grid[r][c - 1]

        return grid[m - 1][n - 1]