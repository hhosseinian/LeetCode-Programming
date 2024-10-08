class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold children nodes
        self.is_end_of_word = False  # Boolean to check if it's the end of a word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node =self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node =node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word,self.root)
    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        for i,char in enumerate(word):
            if char =='.':
                for child in node.children.values():
                    if self._search_in_node(word[i+1:],child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                node = node.children[char]
        return node.is_end_of_word


            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)