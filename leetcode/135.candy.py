#!/usr/bin/python3
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        st = []
        candies = [0]*len(ratings)
        for i in range(len(ratings)):
            if not st or st[-1] >= ratings[i]:
                st.append(ratings[i])
                continue
            
            while st:
                j = st.pop()
                candies[j] = candies[j+1] + 1
        
        print(candies)
        return sum(candies)


if __name__ == '__main__':
    nums = [1, 0, 2]
    ret = Solution().candy(nums)
    print(ret)        
