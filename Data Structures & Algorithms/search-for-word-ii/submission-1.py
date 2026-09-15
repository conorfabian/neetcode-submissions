class TrieNode():

    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        trie = TrieNode()
        for word in words:
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True

        res = set()
        seen = set()
        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in seen or board[r][c] not in node.children:
                return

            seen.add((r, c))
            char = board[r][c]
            word.append(char)

            node = node.children[char]

            if node.end:
                res.add("".join(word))

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            word.pop()
            seen.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie, [])

        return list(res)