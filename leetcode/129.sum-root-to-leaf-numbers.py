#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        st: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]
        ans = 0
        while st:
            node, cur = st.pop()
            v = cur * 10 + node.val
            if not node.left and not node.right:
                ans += v
            else:
                if node.right:
                    st.append((node.right, v))
                if node.left:
                    st.append((node.left, v))
        return ans


# @lc code=end
class P129TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[1,2,3,4,null,5,6,null,null,7]")
        self.assertEqual(124 + 1357 + 136, Solution().sumNumbers(root))

    def test_2(self):
        root = deserialize_tree("[1,2,3]")
        self.assertEqual(25, Solution().sumNumbers(root))

    def test_3(self):
        root = deserialize_tree("[4,9,0,5,1]")
        self.assertEqual(1026, Solution().sumNumbers(root))


if __name__ == "__main__":
    unittest.main()
