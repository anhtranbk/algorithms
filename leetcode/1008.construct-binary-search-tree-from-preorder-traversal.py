#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
from typing import List, Optional

from common import (
    BaseTestCase,
    TreeNode,
    deserialize_tree,
    draw_tree_ascii,
    find_in_bst,
    unittest,
)


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        st = [root]
        for v in preorder[1:]:
            if st[-1].val >= v:
                node = TreeNode(v)
                st[-1].left = node
                st.append(node)
            else:
                while st and st[-1].val < v:
                    node = st.pop()

                new_node = TreeNode(v)
                node.right = new_node
                st.append(new_node)

        return root


# @lc code=end
