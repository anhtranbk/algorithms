#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
from common import BaseTestCase, ListNode
import unittest

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.data = [None]*256 

    def add(self, key: int) -> None:
        idx = key % 256
        curr: ListNode = self.data[idx]
        if not curr:
            curr = ListNode(key)
            return

        if curr.val == key:
            return

        found = False
        while curr.next:
            if curr.next.val == key:
                break
            
            curr = curr.next

        if not found:
            new_node = ListNode(key)
            curr.next = new_node

    def remove(self, key: int) -> None:
        idx = key % 256
        curr: ListNode = self.data[idx]


    def contains(self, key: int) -> bool:
        idx = key % 256
        curr : ListNode = self.data[idx]

        if not curr:
            return False

        if curr.val == key:
            return True

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
