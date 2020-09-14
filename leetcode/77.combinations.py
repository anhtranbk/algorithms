#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

from typing import List
# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans: List[List[int]] = []
        tmp: List[int] = []
        self.do_combine(ans, tmp, n, k, 1)

        return ans
    
    def do_combine(self, ans: List[List[int]], cur: List[int], n: int, k: int, i: int):
        for j in range(i, n+1):
            cur.append(j)
            if k-1 == 0:
                clone = cur.copy()
                ans.append(clone)
            else:
                self.do_combine(ans, cur, n, k-1, j+1)
            
            cur.pop()       
# @lc code=end
if __name__ == '__main__':
    ans = Solution().combine(n=5, k = 3)
    print(ans)
