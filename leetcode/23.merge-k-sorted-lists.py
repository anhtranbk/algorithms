#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            return self.mergeSubKLists(lists, 0, len(lists)-1)
        return None

    def mergeSubKLists(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l == r:
            return lists[l]
        elif l + 1 == r:
            return self.merge2Lists(lists[l], lists[r])
        else:
            m = (l + r) // 2
            left = self.mergeSubKLists(lists, l, m)
            right = self.mergeSubKLists(lists, m+1, r)
            return self.merge2Lists(left, right)

    def merge2Lists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left

        dummy = ListNode()
        node = dummy
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            node.next = left
        if right:
            node.next = right

        return dummy.next

# @lc code=end
class P23TestCase(unittest.TestCase):
    def testMergeKLists(self):
        l1 = self.createListNode([1, 3, 4, 5, 7])
        l2 = self.createListNode([1, 2, 3, 4, 5, 6])
        l3 = self.createListNode([3, 6, 7, 9])
        l4 = self.createListNode([2, 4, 7, 8, 9, 10])
    
        ans = Solution().mergeKLists(lists=[l1, l2, l3, l4])
        
        actual = self.nodeToArray(node=ans)
        expected = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6,7, 7, 7, 8, 9, 9, 10]
        self.assertEquals(actual, expected)
        
    @staticmethod
    def createListNode(vals):
        node = head = ListNode()
        for e in vals:
            next = ListNode(val=e)
            node.next = next
            node = next
        return head.next

    @staticmethod
    def nodeToArray(node: ListNode):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr


if __name__ == '__main__':
    unittest.main()
