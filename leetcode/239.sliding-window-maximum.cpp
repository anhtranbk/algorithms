/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 */
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
   public:
    // https://leetcode.com/problems/sliding-window-maximum/solutions/65898/clean-c-o-n-solution-using-a-deque/
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            if (!dq.empty() && dq.front() == i - k) 
                dq.pop_front();

            while (!dq.empty() && nums[dq.back()] < nums[i])
                dq.pop_back();

            dq.push_back(i);
            if (i >= k - 1) 
                ans.push_back(nums[dq.front()]);
        }
        return ans;
    }

    // O(nlogn) solution using max heap
    vector<int> maxSlidingWindow_maxHeap(vector<int>& nums, int k) {
        priority_queue<tuple<int, int>> pq;
        for (int i = 0; i < k - 1; ++i) {
            pq.push({nums[i], i});
        }

        vector<int> ans(nums.size() - k + 1, 0);
        for (int r = k - 1; r < nums.size(); ++r) {
            pq.push({nums[r], r});
            int l = r - k + 1;

            while (pq.empty() == false && get<1>(pq.top()) < l) {
                pq.pop();
            }

            ans[l] = get<0>(pq.top());
        }

        return ans;
    }
};
// @lc code=end
int main() {
    // vector<int> nums{1, 3, -1, -3, 5, 3, 6, 7};
    vector<int> nums{1, 3, 1, 2, 0, 5};

    Solution sl;
    // vector<int> ans = sl.maxSlidingWindow(nums, 3);
    vector<int> ans = sl.maxSlidingWindow_dequeu(nums, 3);
    // vector<int> ans = sl.maxSlidingWindow_maxHeap(nums, 3);

    cout << "len: " << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
}
