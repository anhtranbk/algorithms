#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
from common import BaseTestCase
import unittest


# @lc code=start
class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        # num2
        # x num1

        tmp = [None] * len(num1)
        for i in range(len(num1)-1, -1, -1):
            tmp[i] = [0] * (len(num2) + 1)
            r = 0
            for j in range(len(num2)-1, -1, -1):
                t = int(num1[i]) * int(num2[j]) + r
                tmp[i][j] = t % 10
                r = t // 10
            tmp[i][-1] = r
            print(tmp[i])
            print(int(num2) * int(num1[i]))

        ans = [0] * (len(num1) + len(num2) + 1)
        r = 0
        for i in range(len(num1)):
            for j in range(len(num2) + 1):
                t = ans[i+j] + tmp[i][j] + r
                ans[i+j] = t % 10
                r = t // 10
        ans[-1] = r

        i = len(ans) - 1
        while ans[i] == 0: i -= 1

        ans = reversed(ans)
        return ''.join([str(e) for e in ans])


# @lc code=end
class P18TestCase(BaseTestCase):

    def test1(self):
        num1, num2 = "123", "456"
        expected = "56088"
        actual = Solution().multiply(num1, num2)
        self.assertEqual(expected, actual)

    # def test2(self):
    #     num1 = "235235"
    #     num2 = "984058320"
    #     expected = int(num1) * int(num2)
    #     actual = Solution().multiply(num1, num2)
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
