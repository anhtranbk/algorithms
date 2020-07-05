#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from multiprocessing import dummy
from common import BaseTestCase, ListNode
import unittest
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.onePassSolution(head, n)

    def onePassSolution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)

        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

    # passed at 10/4/2020
    def stupidSolution(self, head: ListNode, n: int) -> ListNode:
        st = []
        node = head
        while node != None:
            st.append(node)
            node = node.next
        removed = None

        while n > 0:
            removed = st.pop()
            n -= 1

        prev = st.pop() if st else None
        if prev:
            prev.next = removed.next
            
        if st:
            return head
        elif prev:
            return prev
        else:
            return removed.next

# @lc code=end
class P19TestCase(BaseTestCase):
    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main()
