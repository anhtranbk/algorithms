#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
from dis import pretty_flags
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_sequence_nodes(self):
        node = self
        while node:
            print(node.val, end=' ')
            node = node.next
        print()


# @lc code=start
class Solution:
    # Solution 1: for 1 -> k, for each group reverse same as reverse all list
    # Solution 2 (better): count number elements of list, for each group reverse inline
    # Solution 3 (more better): count number elements of list, reverse inline for all elements

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseKGroup(head=head, k=k)

    # TODO: Make better solution works
    def reverseKGroup_better(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cnt, node = 0, head
        while node:
            cnt += 1
            node = node.next

        prev, prev_tail = dummy, dummy
        node = dummy.next
        while cnt >= k:
            for _ in range(0, k):
                cnt -= 1
                next = node
                node.next = prev
                prev = node
                node = next

            t = prev_tail.next
            prev_tail.next = prev
            prev_tail = t

        return dummy.next


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        prev_group = head
        node = head.next

        while True:
            i = 0
            head_group = node
            while node and i < k:
                node = node.next
                i += 1
            if i != k:
                prev_group.next = head_group
                break

            local_head, local_tail = self.reverseLL(head=head_group, k=k)
            prev_group.next = local_head
            prev_group = local_tail

        return head.next


    def reverseLL(self, head: Optional[ListNode], k: int = 9999):
        node: ListNode = head
        prev = None
        i = 0
        while node and i < k:
            next = node.next
            node.next = prev
            prev = node
            node = next
            i += 1
        return prev, head
            
        
# @lc code=end
if __name__ == '__main__':
    head = ListNode()
    node = head
    for n in range(1, 9):
        node.next = ListNode(val=n)
        node = node.next
    
    # head, tail = Solution().reverseLL(head=head.next)
    # head.print_sequence_nodes()

    head = Solution().reverseKGroup(head=head.next, k=3)
    head.print_sequence_nodes()
