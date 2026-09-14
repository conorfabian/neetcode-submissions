class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end

            curr = node
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for _, child in curr.children.items():
                        if dfs(child, j + 1):
                            return True
                    return False
                elif c not in curr.children:
                    return False

                curr = curr.children[c]

            return curr.end

        return dfs(self.root, 0)
        
