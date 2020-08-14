#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from common import BaseTestCase, unittest
from typing import List

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i:] in wordDict:
                dp[i] = 1
                continue
            for j in range(i+1, len(s)):
                if dp[j] == 1 and s[i:j] in wordDict:
                    dp[i] = 1
                    break
        return dp[0] == 1
        
# @lc code=end
class P139TestCase(BaseTestCase):
    def test_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(Solution().wordBreak(s, wordDict))

    def test_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(Solution().wordBreak(s, wordDict))

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(Solution().wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()
