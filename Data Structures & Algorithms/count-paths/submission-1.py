class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        grid[m - 1][n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r + 1 < m:
                    grid[r][c] += grid[r + 1][c]

                if c + 1 < n:
                    grid[r][c] += grid[r][c + 1]

        return grid[0][0]