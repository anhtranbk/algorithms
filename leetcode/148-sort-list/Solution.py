# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        l3 = ListNode(-1)
        head = l3
        while l1 or l2:
            if l1 and (not l2 or l1.val < l2.val):
                l3.next = l1
                l3 = l1
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l2
                l2 = l2.next
        return head.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fast, slow = head, head
        preSlow = slow
        while fast and fast.next:
            fast = fast.next.next
            preSlow = slow
            slow = slow.next
        preSlow.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeTwoLists(left, right)

