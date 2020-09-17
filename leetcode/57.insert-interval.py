#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List
from common import BaseTestCase, unittest

# @lc code=start
class Solution:
    def find_pos(self, intervals: List[List[int]], newInterval: List[int], p: int) -> int:
        if newInterval[p] < intervals[0][p]:
            return 0
        if newInterval[p] > intervals[-1][p]:
            return len(intervals)

        lo, hi, m = 0, len(intervals)-1, 0
        while lo < hi:
            m = lo + (hi-lo)//2
            if intervals[m][p] < newInterval[p]:
                lo = m+1
            elif intervals[m][p] > newInterval[p]:
                hi = m;
            else:
                return m
        return lo
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return[newInterval]

        l = self.find_pos(intervals, newInterval, 0)
        prev = intervals[l-1] if l > 0 else None
        if prev and prev[1] >= newInterval[0]:
            l -= 1

        r = self.find_pos(intervals, newInterval, 1)
        nxt = intervals[r+1] if r < len(intervals)-1 else None
        if nxt and nxt[0] <= newInterval[1]:
            r += 1

        ans = intervals[:l] if l > 0 else []
        ans.append()

        return ans
        
# @lc code=end
class P57TestCase(BaseTestCase):
    def test_1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5] 
        expected = [[1,5],[6,9]]
        actual = Solution().insert(intervals, newInterval)
        
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertArrayEquals(expected[i], actual[i])

    def test_2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        expected = [[1,2],[3,10],[12,16]]
        actual = Solution().insert(intervals, newInterval)
        
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertArrayEquals(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
