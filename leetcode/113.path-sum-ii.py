#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Path Sum I
        """
        if not root: return False
        st = [(root, 0)]
        while st:
            node, xsum = st.pop()
            xsum += node.val
            if xsum == sum and not node.left and not node.right:
                return True
            if node.left:
                st.append((node.left, xsum))
            if node.right:
                st.append((node.right, xsum))
        return False

    def pathSum(self, root: TreeNode, sum: int) -> List[int]:
        """
        Path Sum II
        """
        if not root: return []
        ans = []

        def dfs(node: TreeNode, xsum, nodes):
            xsum += node.val
            nodes.append(node)
            if xsum == sum and not node.left and not node.right:
                ans.append([n.val for n in nodes])
            if node.left:
                dfs(node.left, xsum, nodes)
            if node.right:
                dfs(node.right, xsum, nodes)
            del nodes[-1]

        dfs(root, 0, [])
        return ans

# @lc code=end

