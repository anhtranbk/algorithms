/*
 * @lc app=leetcode id=560 lang=cpp
 *
 * [560] Subarray Sum Equals K
 */
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
   public:
    int subarraySum(vector<int> &nums, int k) {
        unordered_map<int, int> cnt;
        int ans = 0, sum = 0;

        cnt[0] = 1;
        for (auto &n : nums) {
            sum += n;
            if (cnt.find(sum - k) != cnt.end()) {
                ans += cnt[sum - k];
            }
            cnt[sum] += 1;
        }
        return ans;
    }
};
// @lc code=end
int main() {
    vector<int> nums{1, 2, 3};
    int ans = Solution().subarraySum(nums, 3);
    cout << ans << endl;
    return 0;
}
