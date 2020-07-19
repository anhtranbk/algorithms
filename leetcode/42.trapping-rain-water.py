#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from common import BaseTestCase
import unittest
from typing import List, Dict

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0
        st = [0]
        for i in range(1, len(height)):
            while st and height[st[-1]] <= height[i]:
                k = st.pop()
                if not st:
                    break

                j = st[-1]
                trapped =  (i-j-1) * (min(height[i], height[j]) - height[k])
                # print('trapped', j, k, i, trapped)
                ans += trapped
            
            st.append(i)
            # print('append', height[i])
                    
        return ans

        
# @lc code=end
class P42TestCase(BaseTestCase):
    def test1(self):
        arr = [0,1,0,2,1,0,1,3,2,1,2,1]
        actual = Solution().trap(arr)
        expected = 6
        self.assertEqual(expected, actual)

    def test2(self):
        arr = [4,2,0,3,2,5]
        actual = Solution().trap(arr)
        expected = 9
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
