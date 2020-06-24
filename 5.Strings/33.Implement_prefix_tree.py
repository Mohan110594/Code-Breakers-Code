#Time complexity :
#Insert - o(n)
#search-o(n)
#startswith-o(n)

#space complexity :

#Insert - o(n)
#search-o(1)
#startswith-o(1)

class TrieNode:
    def __init__(self):
        self.end=False
        self.children={}
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root1=self.root
        for val in word:
            if val not in root1.children:
                root1.children[val]=TrieNode()
            root1=root1.children[val]
        root1.end=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root1=self.root
        for val in word:
            if val not in root1.children:
                return False
            root1=root1.children[val]
        return root1.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root1=self.root
        for val in prefix:
            if val not in root1.children:
                return False
            root1=root1.children[val]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)