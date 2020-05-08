#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            ans = max(ans, (j - i) * min(height[i], height[j]))
        return ans
        
# @lc code=end
if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ret = Solution().maxArea(height)
    print(ret)
