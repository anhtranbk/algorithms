#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
from typing import Optional

from common import BaseTestCase, unittest


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# @lc code=start
class Solution:
    def connect(self, root: "Node") -> "Node":
        head_nxt: "Node" = root
        # dummy node to avoid creating new head_nxt node (keep O(1) space complexity)
        dummy = Node()
        while head_nxt:
            dummy.next = None
            node, head_nxt, tail_nxt = head_nxt, dummy, dummy
            while node:
                if node.left:
                    tail_nxt.next = node.left
                    tail_nxt = node.left
                if node.right:
                    tail_nxt.next = node.right
                    tail_nxt = node.right
                node = node.next
            # next to right node of dummy node
            head_nxt = head_nxt.next
        return root


# @lc code=end
