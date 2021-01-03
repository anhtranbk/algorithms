#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
from typing import List


# @lc code=start
class Solution:
    # O(nlogn) time, O(n) memory where n = total jobs
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # jobs by start time
        jobs = dict()
        n = len(startTime)
        for i in range(n):
            if startTime[i] in jobs:
                vals = jobs[startTime[i]]
            else:
                vals = []

            vals.append(i)
            jobs[startTime[i]] = vals

        startTimeUniq = list(jobs.keys())
        startTimeUniq.sort()

        def binary_search(nums: list[int], v: int):
            if v > nums[-1]:
                return -1

            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if v < nums[m]:
                    r = m
                elif v > nums[m]:
                    l = m + 1
                else:
                    return nums[m]
            return nums[l]

        dp = {}
        ans = 0
        for i in range(len(startTimeUniq) - 1, -1, -1):
            for jobId in jobs[startTimeUniq[i]]:
                # find nearest start time after current job done
                nextStartTime = binary_search(startTimeUniq, endTime[jobId])
                p = profit[jobId] + dp.get(nextStartTime, 0)
                ans = max(ans, p)
            dp[startTimeUniq[i]] = ans

        return ans


# @lc code=end
