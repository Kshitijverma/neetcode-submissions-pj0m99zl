class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            cur = root

            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for ch in cur.children.values():
                        if dfs(i + 1, ch):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)
