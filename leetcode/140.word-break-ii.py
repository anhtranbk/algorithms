#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from common import BaseTestCase, unittest
from typing import List

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp: List[List[str]] = [[] for _ in range(n)] 
        
        for i in range(n-1, -1, -1):
            v = s[i:]
            if v in wordDict:
                dp[i].append(v)
            for j in range(i+1, n):
                v = s[i:j]
                if dp[j] and v in wordDict:
                    for t in dp[j]:
                        dp[i].append(v + ' ' + t)
                        
        return dp[0]
        
# @lc code=end
class P140TestCase(BaseTestCase):
    def test_1(self):
        s = "catsanddog"
        wordDict = ["cat","cats","and","sand","dog"]
        expected = sorted(["cats and dog","cat sand dog"])
        actual = Solution().wordBreak(s, wordDict)
        self.assertArrayEquals(actual, expected)

    def test_2(self):
        s = "pineapplepenapple"
        wordDict = ["apple","pen","applepen","pine","pineapple"]
        expected = sorted([
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple"
        ])
        actual = Solution().wordBreak(s, wordDict)
        self.assertArrayEquals(actual, expected)

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(0, len(actual))


if __name__ == "__main__":
    unittest.main()
