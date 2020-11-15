#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = dict(), dict()
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for i, c in enumerate(pattern):
            if c in d1 and words[i] in d2:
                if d1[c] != d2[words[i]]:
                    return False
            elif c in d1 or words[i] in d2:
                return False
            else:
                d1[c] = i
                d2[words[i]] = i

        return True


# @lc code=end
class P290TestCase(BaseTestCase):
    def test_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        self.assertTrue(Solution().wordPattern(pattern, s))

    def test_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        self.assertFalse(Solution().wordPattern(pattern, s))

    def test_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        self.assertFalse(Solution().wordPattern(pattern, s))

    def test_4(self):
        pattern = "abbc"
        s = "dog cat cat dog"
        self.assertFalse(Solution().wordPattern(pattern, s))


if __name__ == "__main__":
    unittest.main()
