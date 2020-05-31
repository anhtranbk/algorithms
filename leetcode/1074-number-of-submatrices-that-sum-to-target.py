class Solution:
    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix)+1, len(matrix[0])+1
        psum = [[0]*cols for _ in range(rows)]
        
        for r in range(1, rows):
            t = 0
            for c in range(1, cols):
                t += matrix[r-1][c-1]
                psum[r][c] = psum[r-1][c] + t
        
        ans = 0
        for r1 in range(rows-1):
            for r2 in range(r1+1, rows):
                dp = {0: 1}
                for c in range(1, cols):
                    x = psum[r2][c] - psum[r1][c]
                    if (x-target) in dp: 
                        ans += dp[x-target]
                    dp[x] = dp.get(x, 0) + 1
        return ans

