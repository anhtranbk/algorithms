/*
 * @lc app=leetcode id=33 lang=cpp
 *
 * [33] Search in Rotated Sorted Array
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
        size_t n = nums.size();
        if (n == 1) {
            return nums[0] == target ? 0 : -1;
        }

        int minIdx = findMinIndex(nums);
        int lo = minIdx, hi = minIdx+n-1;
        while (lo < hi) {
            int mid = lo + (hi-lo)/2;
            // calculate real index for m
            int realmid = mid%n;
            if (nums[realmid] == target) return realmid;
            else if (nums[realmid] < target) lo = mid + 1;
            else hi = mid;
        }
        lo %= n;
        return nums[lo] == target ? lo : -1;
    }

    int findMinIndex(vector<int>& nums) {
        int lo = 0, hi = nums.size()-1;
        while (lo < hi) {
            int m = lo + (hi-lo)/2;
            size_t prev = m > 0 ? m-1 : nums.size()-1;
            if (nums[m] < nums[prev] && nums[m] < nums[m+1]) return m;
            if (nums[m] < nums[hi]) hi = m;
            else lo = m+1;
        }
        return lo;
    }
};
// @lc code=end

