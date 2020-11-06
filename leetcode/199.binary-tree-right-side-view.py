#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from typing import List, Optional

from common import BaseTestCase, TreeNode, deserialize_tree, draw_tree_ascii, unittest


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q: Queue[TreeNode] = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            node: Optional[TreeNode] = None
            for _ in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            ans.append(node.val)

        return ans


# @lc code=end
class P199TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[1,2,3,null,5,null,4]")
        self.assertEqual([1, 3, 4], Solution().rightSideView(root))

    def test_2(self):
        root = deserialize_tree("[1,null,3]")
        self.assertEqual([1, 3], Solution().rightSideView(root))

    def test_3(self):
        root = deserialize_tree("[]")
        self.assertEqual(0, len(Solution().rightSideView(root)))


if __name__ == "__main__":
    unittest.main()
