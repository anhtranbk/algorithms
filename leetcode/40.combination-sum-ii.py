#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans, st = [], []

        self.backtracking2(candidates, target, 0, st, ans)

        return ans

    def backtracking(
        self, candidates: List[int], 
        target: int,
        idx: int,
        st: List[int],
        ans: List[List[int]]
    ):
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue

            new_target = target - candidates[i]
            if new_target < 0:
                break

            st.append(candidates[i])

            if new_target == 0:
                ans.append(st.copy())
            elif new_target > 0:
                self.backtracking(candidates, new_target, i+1, st, ans)

            st.pop()

    # More straightforward approach
    def backtracking2(
        self, candidates: List[int], 
        target: int,
        idx: int,
        st: List[int],
        ans: List[List[int]]
    ):
        if target == 0:
            ans.append(st.copy())
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue

            new_target = target - candidates[i]
            if new_target < 0:
                break

            st.append(candidates[i])
            self.backtracking2(candidates, new_target, i+1, st, ans)
            st.pop()


# if __name__ == '__main__':
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # candidates = [2, 5, 2, 1, 2]
    # target = 5
    # ans = Solution().combinationSum2(candidates, target)
    # print(ans)

# @lc code=end

