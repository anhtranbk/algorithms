#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        strs = []
        for d in digits:
            first_digit = not strs
            new_strs = []
            for c in mappings[d]:
                if first_digit:
                    new_strs.append(c)
                else:
                    for s in strs:
                        new_strs.append(s + c)
            strs = new_strs
        return strs
        
# @lc code=end
if __name__ == '__main__':
    print(Solution().letterCombinations('235'))
