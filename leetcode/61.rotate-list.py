#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
from typing import List, Optional
import unittest
from common import BaseTestCase, ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
        # self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        k = k % size
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        head = slow.next
        slow.next = None

        return head


# @lc code=end
class P61TestCase(BaseTestCase):
    def test1(self):
        nums = [1,2,3,4,5]
        dummy = ListNode()
        node = dummy
        for n in nums:
            next_node = ListNode(val=n)
            node.next = next_node
            node = next_node

        ans = Solution().rotateRight(head=dummy.next, k=2)
        expected = [4,5,1,2,3]
        actual = ans.vals_as_array()

        self.assertArrayEquals(expected=expected, actual=actual)

    def test2(self):
        nums = [0,1,2]
        dummy = ListNode()
        node = dummy
        for n in nums:
            next_node = ListNode(val=n)
            node.next = next_node
            node = next_node

        ans = Solution().rotateRight(head=dummy.next, k=4)
        expected = [2,0,1]
        actual = ans.vals_as_array()

        self.assertArrayEquals(expected=expected, actual=actual)

    def test3(self):
        nums = [1,2,3,4,5]
        dummy = ListNode()
        node = dummy
        for n in nums:
            next_node = ListNode(val=n)
            node.next = next_node
            node = next_node

        ans = Solution().rotateRight(head=dummy.next, k=9)
        expected = [2,3,4,5,1]
        actual = ans.vals_as_array()

        self.assertArrayEquals(expected=expected, actual=actual)

    def test4(self):
        nums = [1,2,3,4,5]
        dummy = ListNode()
        node = dummy
        for n in nums:
            next_node = ListNode(val=n)
            node.next = next_node
            node = next_node

        ans = Solution().rotateRight(head=dummy.next, k=10)
        expected = [1,2,3,4,5]
        actual = ans.vals_as_array()

        self.assertArrayEquals(expected=expected, actual=actual)


if __name__ == '__main__':
    unittest.main()
