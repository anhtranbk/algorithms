#include <iostream>
#include <algorithm>

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        std::vector<std::vector<int>> dp(m);
        for (auto i = 0; i < m; ++i) {
            dp[i] = vector<int>(n);
            for (auto j = 0; j < n; ++j) {
                dp[i][j] = -1; 
            }
        }
        dp[m-1][n-1] = grid[m-1][n-1];

        return move(dp, grid, m, n, 0, 0);
    }

private:
    int move(vector<vector<int>>& dp, 
             const vector<vector<int>> &grid,
             int m, int n, int i, int j) {
        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        int mvd = 20001, mvr = 20001;
        if (i+1 < m) {
            mvd = move(dp, grid, m, n, i+1, j);
        }
        if (j+1 < n) {
            mvr = move(dp, grid, m, n, i, j+1);
        }

        dp[i][j] = grid[i][j] + std::min(mvd, mvr);
        return dp[i][j];
    }
};