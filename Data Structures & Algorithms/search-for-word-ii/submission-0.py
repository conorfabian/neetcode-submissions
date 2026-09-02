class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()

        for word in words:
            trie.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, seen = set(), set()
        
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r, c) in seen:
                return

            seen.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            seen.remove((r, c))

            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")

        return list(res)