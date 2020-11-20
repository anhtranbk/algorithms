/*
 * @lc app=leetcode id=378 lang=cpp
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 */
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// @lc code=start
class Solution {
public:
    int kthSmallest(vector<vector<int>> &matrix, int k) {
        return maxHeap_solution(matrix, k);
    }

    int maxHeap_solution(vector<vector<int>> &matrix, int k) {
        int m = matrix.size(), n = matrix[0].size(); // For general, the matrix need not be a square
        priority_queue<int> maxHeap;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                maxHeap.push(matrix[r][c]);
                if (maxHeap.size() > k) maxHeap.pop();
            }
        }
        return maxHeap.top();
    }
};
// @lc code=end

