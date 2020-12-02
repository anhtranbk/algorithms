#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
import unittest
from typing import List, Optional, Tuple

from common import BaseTestCase, TreeNode, deserialize_tree, draw_tree_ascii


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        st: List[Tuple[TreeNode, int]] = [(root, 0)]
        ans, max_lvl = root.val, 0
        while st:
            node, lvl = st.pop()
            # find the most left node of new level
            if node.left and lvl + 1 > max_lvl:
                max_lvl = lvl + 1
                ans = node.left.val
            elif node.right and lvl + 1 > max_lvl:
                max_lvl = lvl + 1
                ans = node.right.val

            if node.right:
                st.append((node.right, lvl + 1))
            if node.left:
                st.append((node.left, lvl + 1))

        return ans


# @lc code=end
class P513TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[1,2,3,4,null,5,6,null,null,7]")
        self.assertEqual(7, Solution().findBottomLeftValue(root))


if __name__ == "__main__":
    unittest.main()
