#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # size of longest subsequence at ith
        dp2 = [1] * n  # number of longest subsequences at ith
        for i in range(n):
            cnt = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt = dp2[j]
                elif dp[j] + 1 == dp[i]:
                    cnt += dp2[j]
            dp2[i] = cnt
        m = max(dp)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == m:
                ans += dp2[i]
        return ans


# @lc code=end
class P673TestCase(BaseTestCase):
    def test_1(self):
        nums = [1, 3, 5, 4, 7]
        self.assertEqual(2, Solution().findNumberOfLIS(nums))

    def test_2(self):
        nums = [2, 2, 2, 2, 2]
        self.assertEqual(5, Solution().findNumberOfLIS(nums))

    def test_3(self):
        nums = [1, 2, 4, 3, 5, 4, 7, 2]
        self.assertEqual(3, Solution().findNumberOfLIS(nums))


if __name__ == "__main__":
    unittest.main()
