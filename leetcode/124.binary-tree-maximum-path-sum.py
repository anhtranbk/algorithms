#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
from typing import List, Optional, Tuple

from common import BaseTestCase, TreeNode, deserialize_tree, draw_tree_ascii, unittest

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

min_int = -2147483648


class Solution:
    def __init__(self):
        self.ans = min_int

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calculate_max_sum(root)
        return self.ans

    def calculate_max_sum(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return min_int

        left = self.calculate_max_sum(node.left)
        right = self.calculate_max_sum(node.right)

        t = max(left, right)
        self.ans = max(self.ans, node.val, t + node.val, left + right + node.val)

        return max(node.val, t + node.val)


# @lc code=end
class P124TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[1,2,3]")
        self.assertEqual(6, Solution().maxPathSum(root))

    def test_2(self):
        root = deserialize_tree("[-10,9,20,null,null,15,7]")
        self.assertEqual(42, Solution().maxPathSum(root))

    def test_3(self):
        root = deserialize_tree("[-3]")
        self.assertEqual(-3, Solution().maxPathSum(root))


if __name__ == "__main__":
    unittest.main()
