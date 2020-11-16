#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# @lc code=start
from queue import Queue
from typing import List, Optional, Tuple

from common import BaseTestCase, TreeNode, deserialize_tree, draw_tree_ascii, unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q: Queue[Tuple[Optional[TreeNode], int]] = Queue()
        q.put((root, 0))

        ans, h = "", self.height(root)

        # level order traversal
        while not q.empty():
            node, lvl = q.get()
            if lvl > h:
                continue
            elif not node:
                ans += "." + ","
                continue

            ans += str(node.val) + ","
            q.put((node.left, lvl + 1))
            q.put((node.right, lvl + 1))

        return ans

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")
        root = TreeNode(vals[0])

        q: Queue[Optional[TreeNode]] = Queue()
        q.put(root)

        for i in range(1, len(vals) - 1, 2):
            node = q.get()
            node.left = TreeNode(int(vals[i])) if vals[i] != "." else None
            node.right = TreeNode(int(vals[i + 1])) if vals[i + 1] != "." else None
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

        return root

    def height(self, root: Optional[TreeNode]):
        return 1 + max(self.height(root.left), self.height(root.right)) if root else -1


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
class P297TestCase(BaseTestCase):
    def test_1(self):
        s = "[1,2,3,4,null,2,4,null,null,4]"
        root = deserialize_tree(s)
        draw_tree_ascii(root, leaf_width=2)

        serialized = Codec().serialize(root)
        print("serialized", serialized)

        deserialized = Codec().deserialize(serialized)
        draw_tree_ascii(deserialized, leaf_width=2)


if __name__ == "__main__":
    unittest.main()
