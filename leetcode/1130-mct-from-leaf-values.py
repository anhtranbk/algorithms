class MedianSortedArrays:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = arr[i] * arr[i+1]
        
        for i in range(1, n):
            dp[0][i] = 