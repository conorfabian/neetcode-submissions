class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        seen = set()
        def dfs(i, j, s):
            if not s:
                return True
            elif i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in seen or board[i][j] != s[0]:
                return False

            seen.add((i, j))
            found = dfs(i - 1, j, s[1:]) or dfs(i + 1, j, s[1:]) or dfs(i, j - 1, s[1:]) or dfs(i, j + 1, s[1:])
            seen.remove((i, j))
            return found

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, word):
                    return True

        return False