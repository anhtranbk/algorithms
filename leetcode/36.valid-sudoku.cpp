/*
 * @lc app=leetcode id=36 lang=cpp
 *
 * [36] Valid Sudoku
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
   public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> rows(9, 0), cols(9, 0), boxes(9, 0);
        for (int i = 0; i < rows.size(); i++) {
            for (int j = 0; j < cols.size(); j++) {
                if (board[i][j] == '.') {
                    continue;
                }

                int v = 1 << (board[i][j] - '0');

                if ((rows[i] & v) > 0)
                    return false;

                if ((cols[j] & v) > 0)
                    return false;

                int k = (i / 3) * 3 + (j / 3);
                if ((boxes[k] & v) > 0)
                    return false;

                rows[i] |= v;
                cols[j] |= v;
                boxes[k] |= v;
            }
        }
        return true;
    }
};
// @lc code=end
