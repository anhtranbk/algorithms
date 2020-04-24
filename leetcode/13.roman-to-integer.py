#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
import unittest

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        return self.solveBetter(s)

    def solve(self, s: str) -> int:
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        prefixables = ('I', 'X', 'C')
        while i < len(s):
            if s[i] in prefixables:
                if i+1 < len(s) and roman[s[i+1]] > roman[s[i]]:
                    ans += roman[s[i+1]] - roman[s[i]]
                    i += 2
                else:
                    ans += roman[s[i]]
                    i += 1
            else:
                ans += roman[s[i]]
                i += 1

        return ans

    # Very very creatite way
    def solveBetter(self, s: str) -> int:
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        return ans + roman[s[-1]]


# if __name__ == '__main__':
    # s = 'LVIII'
    # s = 'MCMXCIV'
    # ans = Solution().romanToInt(s)
    # print(ans)
        
# @lc code=end
class P23TestCase(unittest.TestCase):
    def testRomanToInteger(self):
        actual = Solution().romanToInt('LVIII')
        self.assertEquals(actual, 58)

        actual = Solution().romanToInt('MCMXCIV')
        self.assertEqual(actual, 1994)


if __name__ == '__main__':
    unittest.main()
