#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List
from common import BaseTestCase, unittest

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children: List[TrieNode] = [None]*26
        self.word: str = ''

    def add_child(self, val):
        i = ord(val[0]) - ord('a') 
        assert len(val) == 1
        assert i >= 0 and i <= 26 

        if self.children[i] is None:
            self.children[i] = TrieNode()
            
        return self.children[i]
    
    def find_child(self, val):
        i = ord(val[0]) - ord('a') 
        assert len(val) == 1
        assert i >= 0 and i <= 26 

        return self.children[i]


# Trie + Backtracking
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)

        ans = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.backtracking(board, i, j, root, ans)

        return ans

    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node = node.add_child(c) 
            node.word = word
        return root
                
    def backtracking(self, 
                     board: List[List[str]], 
                     i: int,
                     j: int,
                     node: TrieNode,
                     ans: List[str]): 
        
        if i < 0 or i == len(board): # out of square
            return
        
        if j < 0 or j == len(board[0]): # out of square
            return
        
        if board[i][j] == '#':
            return
        
        c = board[i][j]
        node = node.find_child(c)
        if node is None:
            return

        if node.word:
            ans.append(node.word)
            node.word = ''

        board[i][j] = '#'

        self.backtracking(board, i-1, j, node, ans)
        self.backtracking(board, i+1, j, node, ans)
        self.backtracking(board, i, j-1, node, ans)
        self.backtracking(board, i, j+1, node, ans)

        board[i][j] = c

    
# @lc code=end
# Backtracking - Time Limit Exceeded
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if self.exist(board, word):
                ans.append(word)
                
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.backtracking(board, word, visited, i, j, 0):
                    return True 

        return False
    
    def backtracking(self, 
                     board: List[List[str]], 
                     word: str,
                     visited: List[List[int]],
                     i: int,
                     j: int,
                     k: int) -> bool:
                    
        if i < 0 or i == len(board):
            return False
        
        if j < 0 or j == len(board[0]):
            return False 
        
        if visited[i][j] == 1:
            return False

        if k == len(word)-1:
            return board[i][j] == word[k] 

        if board[i][j] != word[k]:
            return False


        visited[i][j] = 1

        if self.backtracking(board, word, visited, i-1, j, k+1):
            return True
        
        if self.backtracking(board, word, visited, i+1, j, k+1):
            return True
         
        if self.backtracking(board, word, visited, i, j-1, k+1):
            return True
                 
        if self.backtracking(board, word, visited, i, j+1, k+1):
            return True

        visited[i][j] = 0
        

class P212TestCase(BaseTestCase):
    def test_1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        expected = ["eat", "oath"]
        actual = Solution().findWords(board, words)
        self.assertArrayEquals(expected, actual, sorted_before_comparing=True)

    def test_2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        actual = Solution().findWords(board, words)
        self.assertArrayEquals([], actual, sorted_before_comparing=True)


if __name__ == "__main__":
    unittest.main()