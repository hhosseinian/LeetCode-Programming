class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] =TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie =Trie()
        for word in words:
            trie.insert(word)
        self.result =set()
        self.row,self.col = len(board),len(board[0])
        self.board =board
        def backtrack(x,y,node,path):
            if node.is_end_of_word:
                self.result.add(path)
                node.is_end_of_word=False
            if x<0 or y<0 or x>=self.row or y>=self.col:
                return
            if board[x][y] =="#":
                return
            char =board[x][y]
            node =node.children.get(char)
            if not node:
                return
            board[x][y] ="#"
            path+=char
            backtrack(x+1,y,node,path)
            backtrack(x-1,y,node,path)
            backtrack(x,y-1,node,path)
            backtrack(x,y+1,node,path)
            board[x][y]=char
        for i in range(self.row):
            for j in range(self.col):
                backtrack(i,j,trie.root,"")
        return list(self.result)

