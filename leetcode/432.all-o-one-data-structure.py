#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
from typing import List, Dict

# @lc code=start
class Node:
    def __init__(self) -> None:
        self.keys = set()
        self.freq = 0
        self.next = None
        self.prev = None

    def add_key(self, key):
        self.keys.add(key)

    def remove_key(self, key):
        self.keys.remove(key)

        
class DoubleLinkedList:
    def __init__(self) -> None:
        self.dummy = Node()

    
        
        
        
class AllOne:

    def __init__(self):
        self.map: Dict[str, Node] = dict()
        self.list = DoubleLinkedList()     

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            if not node.next:
                nxt =  

    def dec(self, key: str) -> None:
        

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

