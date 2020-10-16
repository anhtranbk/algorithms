#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# @lc code=start
from queue import SimpleQueue
from typing import List, Optional

from common import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = SimpleQueue()
        q.put(root)

        ans = []
        while not q.empty():
            ret = []
            for _ in range(0, q.qsize()):
                node = q.get()
                ret.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(ret)
        return ans


# @lc code=end
