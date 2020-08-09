#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional
from common import unittest, BaseTestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(node: TreeNode) -> TreeNode:
            l: TreeNode = node.left
            r: TreeNode = node.right

            if l: 
                node.right = l
                node.left = None
                node = dfs(l)

            if r:
                node.right = r
                node.left = None
                node = dfs(r) 

            return node
        
        dfs(root)
        
        
# @lc code=end

