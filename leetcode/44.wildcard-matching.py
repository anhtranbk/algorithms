#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatch0(s, p, 0, 0)

    def isMatch0(self, s: str, p: str, i: int, j: int) -> bool:
        while i < len(s) and j < len(p):
            if p[j] == '*':
                if j+1 == len(p):
                    return True
                elif p[j+1] == s[i]:
                    ok = self.isMatch(s, p, i, j+1)
                    if ok:
                        return True
                    else:
                        i += 1
            elif p[j] == '?' or s[i] == p[j]:
                i += 1
                j += 1
            else:
                return False
        return not len(s)

        
# @lc code=end

