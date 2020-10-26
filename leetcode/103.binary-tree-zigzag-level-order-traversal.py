#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
from typing import List, Optional

from common import BaseTestCase, TreeNode, deserialize_tree, draw_tree_ascii, unittest


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # using two stack
        zig, zag = [root], []
        ans, reverse = [], -1
        while zig or zag:
            t = []
            cur = zag if reverse > 0 else zig
            nxt = zig if reverse > 0 else zag
            for _ in range(len(cur)):
                node = cur.pop()
                t.append(node.val)
                if reverse > 0:
                    children = [node.right, node.left]
                else:
                    children = [node.left, node.right]
                for c in children:
                    if c:
                        nxt.append(c)
            reverse *= -1
            if t:
                ans.append(t)

        return ans


# @lc code=end
class P103TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[3,9,20,null,null,15,7]")
        expected = [[3], [20, 9], [15, 7]]
        actual = Solution().zigzagLevelOrder(root)
        self.assertEqual(expected, actual)

    def test_2(self):
        root = deserialize_tree("[1]")
        expected = [[1]]
        actual = Solution().zigzagLevelOrder(root)
        self.assertEqual(expected, actual)

    def test_3(self):
        root = deserialize_tree("[]")
        actual = Solution().zigzagLevelOrder(root)
        self.assertEqual(0, len(actual))

    def test_4(self):
        root = deserialize_tree("[1,2,3,null,5,null,4]")
        expected = [[1], [3, 2], [5, 4]]
        actual = Solution().zigzagLevelOrder(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
