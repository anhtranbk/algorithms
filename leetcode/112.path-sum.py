#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


 # @lc code=start       
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        st = [(root, 0)]
        while st:
            node, xsum = st.pop()
            xsum += node.val
            if xsum == targetSum and not node.left and not node.right: 
                return True
            if node.left:
                st.append((node.left, xsum))
            if node.right:
                st.append((node.right, xsum))
        return False
# @lc code=end

