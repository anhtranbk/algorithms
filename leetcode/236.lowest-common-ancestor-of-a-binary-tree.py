#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
from common import (
    BaseTestCase,
    TreeNode,
    deserialize_tree,
    draw_tree_ascii,
    find_in_binary_tree,
    unittest,
)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Note that this solution only works if the following conditions are satisfied:
        # - all node.val are unique
        # - p != q
        # q and q must be exist in the tree
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # becase p != q:
        # if l and r are not null
        # -> it means that p and q in two sides of the current node -> current node is LCA
        # if only l or r is not null
        # -> it means that p and q in same side of the current node -> l or r is LCA
        if l and r:
            return root
        else:
            return l or r


# @lc code=end
class P236TestCase(BaseTestCase):
    def test_1(self):
        root = deserialize_tree("[3,5,1,6,2,0,8,null,null,7,4]")
        p = find_in_binary_tree(root, 5)
        q = find_in_binary_tree(root, 1)
        self.assertEqual(3, Solution().lowestCommonAncestor(root, p, q).val)

    def test_2(self):
        root = deserialize_tree("[3,5,1,6,2,0,8,null,null,7,4]")
        p = find_in_binary_tree(root, 5)
        q = find_in_binary_tree(root, 4)
        self.assertEqual(5, Solution().lowestCommonAncestor(root, p, q).val)

    def test_3(self):
        root = deserialize_tree("[1,2]")
        p = find_in_binary_tree(root, 2)
        q = find_in_binary_tree(root, 1)
        self.assertEqual(1, Solution().lowestCommonAncestor(root, p, q).val)

    def test_4(self):
        root = deserialize_tree("[3,5,1,6,2,0,8,null,null,7,4]")
        p = find_in_binary_tree(root, 6)
        q = find_in_binary_tree(root, 4)
        self.assertEqual(5, Solution().lowestCommonAncestor(root, p, q).val)

    def test_5(self):
        root = deserialize_tree("[3,5,1,6,2,0,8,null,null,7,4]")
        p = find_in_binary_tree(root, 7)
        q = find_in_binary_tree(root, 8)
        self.assertEqual(3, Solution().lowestCommonAncestor(root, p, q).val)


if __name__ == "__main__":
    unittest.main()
