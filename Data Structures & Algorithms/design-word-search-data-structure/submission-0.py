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

        def helper(i, node):
            if i == len(word):
                return node.end
            
            c = word[i]
            if c in node.children:
                return helper(i + 1, node.children[c])
            elif c == ".":
                for child in node.children.values():
                    if helper(i + 1, child):
                        return True

            return False


        return helper(0, self.root)
        
