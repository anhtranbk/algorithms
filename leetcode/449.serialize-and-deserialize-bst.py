#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#
from typing import List, Optional

from common import BaseTestCase, TreeNode, deserialize_tree, drawtree, unittest

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        st, ans = [root], ""
        while st:
            node: TreeNode = st.pop()
            ans += str(node.val) + ","
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return ans[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        vals = [int(v) for v in data.split(",")]
        root = TreeNode(vals[0])

        st = [root]
        for v in vals[1:]:
            if v <= st[-1].val:
                node = TreeNode(v)
                st[-1].left = node
                # print('added {} to the left of {}'.format(node, st[-1]))
                st.append(node)
            else:
                while st and st[-1].val < v:
                    node = st.pop()

                new_node = TreeNode(v)
                node.right = new_node
                # print('added {} to the right of {}'.format(new_node, node))
                st.append(new_node)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end
class P449TestCase(BaseTestCase):
    def test_1(self):
        v100 = TreeNode(100)

        v30 = TreeNode(30)
        v20 = TreeNode(20)
        v20.right = v30
        v10 = TreeNode(10)
        v10.right = v20
        v100.left = v10

        v150 = TreeNode(150)
        v200 = TreeNode(200)
        v200.left = v150
        v300 = TreeNode(300)
        v300.left = v200
        v100.right = v300

        serialized = Codec().serialize(v100)
        print("serialized: ", serialized)

        deserialized = Codec().deserialize(serialized)
        print("deserialized: ", Codec().serialize(deserialized))

    def test_2(self):
        s = "[41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]"
        serialized = Codec().serialize(deserialize_tree(s))
        print("serialized", serialized)
        Codec().deserialize(serialized)


if __name__ == "__main__":
    unittest.main()
