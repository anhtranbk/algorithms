#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
from typing import List, Optional

from common import BaseTestCase, TreeNode, unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.iterative(root, key)

    def iterative(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr, pre = root, None
        while curr and curr.val != key:
            pre = curr
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left

        if not curr:
            return root
        if not pre:
            return self.do_delete(curr)

        if pre.left == curr:
            pre.left = self.do_delete(curr)
        else:
            pre.right = self.do_delete(curr)

        return root

    def recursive(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # find node to delete in right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # find node to delete in left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root = self.do_delete(root)

        return root

    def do_delete(self, node: TreeNode) -> Optional[TreeNode]:
        if not node.left and not node.right:
            return None
        elif not node.right:
            return node.left
        elif not node.left:
            return node.right
        else:
            # IMPORTANT: max left node in left side or min leaf node in right side will be new root of subtree
            # steps
            # - swap node to be deleted with left (just swap value)
            # - remove left node
            tmp = self.find_min(node.right)
            node.val = tmp.val
            node.right = self.deleteNode(node.right, tmp.val)
            return node

    def find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def find_max(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node


# @lc code=end
