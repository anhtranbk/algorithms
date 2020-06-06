#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans, st = [], []
        self.process(candidates, target, 0, st, ans)
        return ans

    def process(
        self, candidates: List[int], 
        target: int,
        idx: int,
        st: List[int],
        ans: List[List[int]]
    ):
        for i in range(idx, len(candidates)):
            target -= candidates[i]
            if target < 0:
                break
            
            st.append(candidates[i])
            if target == 0:
                ans.append(st.copy())
            elif target > 0:
                self.process(candidates, target, i, st, ans)
            target += candidates[i]
            st.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    # candidates = [2, 3, 5]
    ans = Solution().combinationSum(candidates=candidates, target=7)
    print(ans)

# @lc code=end

