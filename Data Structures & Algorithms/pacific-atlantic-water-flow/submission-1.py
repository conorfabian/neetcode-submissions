class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, seen, prevHeight):
            if ((r, c) in seen) or (r < 0) or (c < 0) or (r == ROWS) or (c == COLS) or heights[r][c] < prevHeight:
                return

            seen.add((r, c))
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r + 1, c, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])

            return

        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)

        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)

        res = []
        for square in pac:
            if square in atl:
                res.append([square[0], square[1]])

        return res