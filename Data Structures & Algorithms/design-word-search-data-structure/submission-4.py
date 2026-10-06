class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, curr):
            while i < len(word):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif word[i] in curr.children:
                    curr = curr.children[word[i]]
                    i += 1
                else:
                    return False

            return curr.word

        return dfs(0, self.root)