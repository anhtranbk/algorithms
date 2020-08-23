#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from typing import List, Tuple
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

    def empty(self) -> bool:
        return len(self.nums) == 0


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = PriorityQueue()
        for r in range(k-1):
            pq.push(r, priority=(-1)*nums[r])

        ans = [0]*(n-k+1)
        l = 0
        for r in range(k-1, n):
            pq.push(r, priority=(-1)*nums[r])
            while not pq.empty() and pq.top()[1] < l:
                pq.pop()

            _, idx = pq.top()
            ans[l] = nums[idx]
            l += 1
        
        return ans            
        
# @lc code=end
class P239TestCase(BaseTestCase):
    def test_1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7]
        actual = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, k = [1], 1
        actual = Solution().maxSlidingWindow(nums, k)
        self.assertEqual([1], actual)

    def test_3(self):
        nums, k = [1,3,1,2,0,5], 3
        actual = Solution().maxSlidingWindow(nums, k)
        expected = [3,3,2,5]
        self.assertEqual(expected, actual)
    
    
if __name__ == "__main__":
    unittest.main()
