#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
from common import BaseTestCase, unittest

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = [[]]
        self.backtracking(ans, [], nums, 0)
        return ans
    
    def backtracking(self, ans: List[List[int]], curr: List[int], nums: List[int], l: int):
        for i in range(l, len(nums)):
            curr.append(nums[i])
            ans.append(curr.copy())
            self.backtracking(ans, curr, nums, i+1)
            curr.pop() 
        
        
# @lc code=end
class P78TestCase(BaseTestCase):
    def test_1(self):
        expected = Solution().subsets([1,2,3])
        print(expected)
    
    def test_2(self):
        expected = Solution().subsets([0])
        print(expected)

        
if __name__ == "__main__":
    unittest.main()
