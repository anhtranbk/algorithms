#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from common import BaseTestCase, unittest
from typing import List, Dict

# 
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected = [0]*58 # ord('z') - ord('A') = 58
        # count the frequency of characters in t
        for c in t:
            self.inc_freq(expected, c)
        
        i, j, missing = 0, 0, len(t)
        actual = [0]*58
        ans = ''
        # we use two pointers i, j to indicate sliding window
        # if all characters of t are included in current window we increse j until enough characters 
        # or the end of the string is reached
        # while all characters of t are still being included in current window we increase to find the minimum window
        # repeat two steps
        for j in range(len(s)):
            c = s[j]
            self.inc_freq(actual, c)
            # if the number of frequence of a particular character is less than or equals to 
            # what actually needed we decrease missing to 1
            if self.get_freq(actual, c) <= self.get_freq(expected, c):
                missing -= 1            

            # increase i (the left size of the window) while missing = 0 to find the minimum window
            while missing == 0 and i <= j:
                c = s[i]
                if self.get_freq(actual, c) == self.get_freq(expected, c):
                    missing += 1
                    l = j - i + 1
                    if not ans or l < len(ans):
                        ans = s[i:j+1]

                self.dec_freq(actual, c)
                i += 1

        return ans
    
    def get_freq(self, freq: List[int], c: str) -> int:
        return freq[ord(c) - ord('A')] 

    def inc_freq(self, freq: List[int], c: str):
        freq[ord(c) - ord('A')] += 1

    def dec_freq(self, freq: List[int], c: str):
        freq[ord(c) - ord('A')] -= 1
                
        
# @lc code=end
class P76TestCase(BaseTestCase):
    def test_1(self):
        s = 'ADOBECODEBANC'
        t = 'ABC'
        expected = 'BANC'
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = 'a'
        t = 'a'
        expected = 'a'
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = 'a'
        t = 'aa'
        actual = Solution().minWindow(s, t)
        self.assertEqual(0, len(actual))


if __name__ == '__main__':
    unittest.main()