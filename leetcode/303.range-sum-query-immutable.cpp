/*
 * @lc app=leetcode id=303 lang=cpp
 *
 * [303] Range Sum Query - Immutable
 */
#include <vector>
#include <iostream>

using namespace std;

// @lc code=start
class NumArray {
public:
    NumArray(vector<int>& nums) {
        sums.push_back(0);
        sums.push_back(nums[0]);
        for (int i = 1; i < nums.size(); ++i) {
            sums.push_back(sums[i] + nums[i]);
        }
    }
    
    int sumRange(int left, int right) {
        return sums[right+1] - sums[left];
    }
private:
    vector<int> sums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
// @lc code=end
int main (int argc, char *argv[]) {
    vector<int> nums;
    for (int i = 0; i < 10; i++) {
            nums.push_back(i+1);
    }

    // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    NumArray numArray(nums);
    int sum = numArray.sumRange(2, 5);
    cout << sum << endl;
}
