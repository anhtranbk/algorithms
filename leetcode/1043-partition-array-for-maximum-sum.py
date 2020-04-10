from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        pass


if __name__ == '__main__':
    arr = [1,15,7,9,2,5,10]
    k = 3
    # arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
    ret = Solution().maxSumAfterPartitioning(arr, k)
    print(ret)
