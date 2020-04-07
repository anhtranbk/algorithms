#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
from typing import List

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(dp: List[List[int]], i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            if j < len(p)-1 and p[j+1] == '*':
                return dfs(i, j+1)

            if i == len(s):
                return p[j] == '*' and j == len(p) - 1
            
            if s[i] == p[j] or p[j] == '.':
                return dfs(i+1, j+1)

            elif p[j] == '*':
                if p[j-1] == '.' or p[j-1] == s[i]:
                    if dfs(i+1, j): # match one and more characters
                        return True
                    elif dfs(i+1, j+1): # match only one
                        return True
                    else:
                        return dfs(i, j+1) # match zero
                else:
                    return dfs(i, j+1)

            return False

        return dfs(0, 0)


# if __name__ == '__main__':
#     s = 'ab'
#     p = '.*'
#     ans = Solution().isMatch(s, p)
#     print(ans)
        
# @lc code=end

