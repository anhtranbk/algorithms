impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        
    }

    fn move(dp: &mut [&mut [i32]], i: i32, j: i32) -> i32 {
        if dp[i][j] != -1 {
            return dp[i][j];
        }

        let mvr = if j == n-1 { 0 } else { move(i, j+1) };
        let mvd = if i == m-1 { 0 } else { move(i+1, j) };

        dp[i][j] = mvr + mvd;

        dp[i][j]
    }
}