#include <algorithm>  

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        int dp[size];
        for (int i = 0; i < size; i++) {
            dp[i] = 1;
        }
        for (int i = nums.size()-2; i >= 0; --i) {
            for (int j = i+1; j < size; ++j) {
                if (nums[i] < nums[j]) {
                    dp[i] = std::max(dp[i], dp[j]+1);
                }
            }
        }
        return *std::max_element(dp, dp+size);
    }
};
