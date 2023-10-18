class TrieNode:
    def __init__(self, value='') -> None:
        self.value = value
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.
        """
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TrieNode(word[:i+1])
            curr = curr.children[char]
        curr.is_word = True
        return curr


    def find(self, word):
        """
        Finds and returns a trie node for the given word.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]

        return curr if curr.is_word else None
