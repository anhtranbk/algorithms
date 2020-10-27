#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import SimpleQueue
from typing import List, Optional

from common import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return reversed(ans)


# @lc code=end
