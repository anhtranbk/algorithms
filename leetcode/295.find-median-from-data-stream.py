#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
from typing import List, Tuple, Dict
from common import BaseTestCase, unittest
# @lc code=start
import heapq


class PriorityQueue:
    def __init__(self):
        self.nums: List[int] = []
        
    def push(self, data, priority=0):
        heapq.heappush(self.nums, (priority, data)) 

    def pop(self) -> Tuple[int, any]:
        return heapq.heappop(self.nums)

    def top(self) -> Tuple[int, any]:
        if self.nums:
            return self.nums[0]
        else:
            return None, None

    def size(self) -> int:
        return len(self.nums)

    def empty(self) -> bool:
        return len(self.nums) == 0

class MedianFinder:

    def __init__(self):
        self.lheap = PriorityQueue()
        self.rheap = PriorityQueue()
        

    def addNum(self, num: int) -> None:
        _, r = self.rheap.top()
        if r is not None and num > r:
            self.rheap.push(num)
        else:
            self.lheap.push(num, -1*num)

        if self.lheap.size() > self.rheap.size() + 1:
            self.rheap.push(self.lheap.pop()[1])
        elif self.lheap.size() < self.rheap.size():
            _, v = self.rheap.pop()
            self.lheap.push(v, priority=(-1)*v) 
        

    def findMedian(self) -> float:
        assert self.lheap.size() >= self.rheap.size()
        if self.lheap.size() > self.rheap.size():
            return self.lheap.top()[1]  
        else:
            return (self.lheap.top()[1] + self.rheap.top()[1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
class P295TestCase(BaseTestCase):
    def test_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())

        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())

        mf.addNum(4)
        self.assertEqual(3, mf.findMedian())

        mf.addNum(5)
        self.assertEqual(3.5, mf.findMedian())
        
        mf.addNum(7)
        self.assertEqual(4, mf.findMedian())

        mf.addNum(9)
        self.assertEqual(4.5, mf.findMedian())

        mf.addNum(10)
        self.assertEqual(5, mf.findMedian())


if __name__ == '__main__':
    unittest.main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
