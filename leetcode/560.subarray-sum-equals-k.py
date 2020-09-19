from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = Counter({0: 1})
        ans = xsum = 0
        for i in range(0, len(nums)):
            xsum += nums[i]
            ans += ct[xsum - k]
            ct[xsum] += 1
        return ans

