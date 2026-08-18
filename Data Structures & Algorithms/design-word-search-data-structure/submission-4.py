class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): #looped over the entire word
                return node.endOfWord

            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if char not in node.children:
                return False

            return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)
