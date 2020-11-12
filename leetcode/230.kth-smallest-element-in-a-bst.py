#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
from typing import Optional

from common import BaseTestCase, unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrderTraversal(root, k)

    def inOrderTraversal(self, root: Optional[TreeNode], k: int) -> int:
        st, cnt, ans = [root], 0, -1
        while st:
            v = st.pop()
            if isinstance(v, int):
                cnt += 1
                if cnt == k:
                    ans = v
                    break
            else:
                node: TreeNode = v
                if node.right:
                    st.append(node.right)
                st.append(node.val)
                if node.left:
                    st.append(node.left)
        return ans


# @lc code=end
