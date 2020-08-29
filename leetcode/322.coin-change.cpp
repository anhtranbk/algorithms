/*
 * @lc app=leetcode id=322 lang=cpp
 *
 * [322] Coin Change
 */
#include <algorithm>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
   public:
    int coinChange(vector<int>& coins, int n) {
        vector<int> dp(n + 1, 10001);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (auto c : coins) {
                int j = i - c;
                if (j >= 0) {
                    dp[i] = min(dp[i], 1 + dp[j]);
                }
            }
        }

        return (dp[n] < 10001) ? dp[n] : -1;
    }
};
// @lc code=end
int main() {
    Solution sl;
    vector<int> coins = {1};
    cout << "fucking result: " << sl.coinChange(coins, 2) << endl;
}
