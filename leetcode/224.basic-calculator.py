#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
from typing import List, Union

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        st = []
        for t in tokens:
            if t == "(":
                st.append(t)
            elif t == ")":
                v = st.pop()
                st.pop()
                self.process_number(st, v)
            elif t == "+" or t == "-":
                st.append(t)
            else:
                self.process_number(st, t)

        return st.pop()

    def process_number(self, st: List[Union[str, int]], t: Union[str, int]):
        if not st or st[-1] == "(":
            st.append(t)
            return

        op = st.pop()
        if op == "+":
            left = st.pop()
            st.append(left + t)
        elif st and isinstance(st[-1], int):
            left = st.pop()
            st.append(left - t)
        else:
            st.append(-1 * t)

    def tokenize(self, s: str) -> List[Union[str, int]]:
        i, tokens = 0, []
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i] == "+" or s[i] == "-" or s[i] == "(" or s[i] == ")":
                tokens.append(s[i])
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                tokens.append(int(s[i:j]))
                i = j
        return tokens


# @lc code=end
class P224TestCase(BaseTestCase):
    def test_1(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))

    def test_2(self):
        self.assertEqual(3, Solution().calculate(" 2-1 + 2 "))

    def test_3(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_4(self):
        exp = "-(54+42- 23 ) - (41 +4  -(21+3)-7) - (-33 +2+99) - 123"
        expected = eval(exp)
        actual = Solution().calculate(exp)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
