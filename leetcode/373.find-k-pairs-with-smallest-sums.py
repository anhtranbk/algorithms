#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from common import BaseTestCase, unittest
from typing import List

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pass
        

# @lc code=end
class P373TestCase(BaseTestCase):
    def test_1(self):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3
        expected = [[1,2],[1,4],[1,6]]
        actual = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertArrayEquals(actual, expected)

    def test_2(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2
        expected = [[1,1],[1,1]]
        actual = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertArrayEquals(actual, expected)
    
    def test_3(self):
        nums1 = [1,2]
        nums2 = [3]
        k = 3
        expected = [[1,3],[2,3]]
        actual = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertArrayEquals(actual, expected)


if __name__ == "__main__":
    unittest.main()