#!/usr/bin/python3
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                ans[i] = ans[i-1] + 1
            else:
                j = i
                while j > 0 and ratings[j-1] > ratings[j] and ans[j-1] <= ans[j]:
                    ans[j-1] = ans[j] + 1
                    j -= 1
        print(ans)
        return sum(ans)


if __name__ == '__main__':
    nums = [1, 2, 2]
    ret = Solution().candy(nums)
    print(ret)        
