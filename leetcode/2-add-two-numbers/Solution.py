# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = l3 = ListNode(0)
        r = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + r
            r, val = divmod(val, 10)
            node = ListNode(val)
            l3.next = node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next
            
        if r:
            l3.next = ListNode(r)
        return dummy.next