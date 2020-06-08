#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        st, ans = [], []
        self.backtracking(k, n, 1, st, ans)
        return ans

    def backtracking(
        self, k: int, 
        n: int,
        idx: int,
        st: List[int],
        ans: List[List[int]]
    ):
        if k == 0:
            if n == 0: 
                ans.append(st.copy())
            return

        k -= 1
        for i in range(idx, 10):
            if n - i < 0:
                break

            st.append(i)
            self.backtracking(k, n-i, i+1, st, ans)
            st.pop()

        
# @lc code=end
if __name__ == '__main__':
    ans = Solution().combinationSum3(k=3, n=7)
    print(ans)
