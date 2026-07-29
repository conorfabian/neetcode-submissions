class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    q = deque([(i, j)])
                    while q:
                        row, col = q.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            grid[row - 1][col] = "0"
                            q.append((row - 1, col))
                        if row + 1 < len(grid) and grid[row + 1][col] == "1":
                            grid[row + 1][col] = "0"
                            q.append((row + 1, col))
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            grid[row][col - 1] = "0"
                            q.append((row, col - 1))
                        if col + 1 < len(grid[0]) and grid[row][col + 1] == "1":
                            grid[row][col + 1] = "0"
                            q.append((row, col + 1))

        return res