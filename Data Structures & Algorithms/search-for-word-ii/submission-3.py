class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.addWord(word)

        res, seen = set(), set()
        def dfs(r, c, node, word):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in seen or board[r][c] not in node.children:
                return 

            seen.add((r, c))
            word.append(board[r][c])
            node = node.children[board[r][c]]
            if node.word:
                res.add("".join(word))
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            seen.remove((r, c))
            word.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root, [])

        return list(res)