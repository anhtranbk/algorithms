#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.dpSolution2(n=n)

    # https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
    def dpSolution3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

    # Based on the solution of a member in LeetCode discusstion
    def dpSolution2(self, n: int) -> List[int]:
        dp = [[] for _ in range(n+1)]
        dp[0] = ['']

        for i in range(1, n+1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i-j]:
                        dp[i].append(x + y)

            for x in dp[i-1]:    
                dp[i].append('(' + x + ')')

            dp[i] = list(set(dp[i]))

        return dp[n]

    def dpSolution(self, n: int) -> List[str]:
        dp = [[] for _ in range(n)]
        dp[0] = ["()"]

        for i in range(1, n):
            parenthesis = set()
            for p in dp[i-1]:
                parenthesis.add(p + '()')
                parenthesis.add('(' + p + ')')
                cnt = 0
                for j in range(0, len(p)):
                    if not cnt:
                        t = '({}){}'.format(p[:j], p[j:])
                        parenthesis.add(t)
                    cnt += 1 if p[j] == '(' else -1

            dp[i] = list(parenthesis)

        return dp[-1]

# @lc code=end
class P22TestCase(unittest.TestCase):
    def test1(self):
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        actual = Solution().generateParenthesis(n=3)
        self.assertArrayEquals(expected, actual)

    def test2(self):
        expected = ["()"]
        actual = Solution().generateParenthesis(n=1)
        self.assertArrayEquals(expected, actual)

    def test3(self):
        expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        actual = Solution().generateParenthesis(n=4)
        self.assertArrayEquals(expected, actual)        

    def assertArrayEquals(self, expected, actual):
        self.assertEqual(len(expected), len(actual))

        expected = sorted(expected)
        actual = sorted(actual)
        # print(actual)
        # print(expected)
        for i in range(0, len(expected)):
            try:
                self.assertEqual(expected[i], actual[i])
            except Exception:
                print('Exception when assert at element ' + str(i))
                raise
        

if __name__ == "__main__":
    unittest.main()
