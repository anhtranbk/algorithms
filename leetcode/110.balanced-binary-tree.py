#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        low, hi, st = 5000, 0, [(root, 1)]
        while st:
            node, h = st.pop()
            if node.left or node.right:
                if node.right:
                    st.append((node.right, h + 1))
                if node.left:
                    st.append((node.left, h + 1))
            else:
                low = min(low, h)
                hi = max(hi, h) 

        print(low, hi)
        return hi - low <= 1
        
# @lc code=end

