/*
 * @lc app=leetcode id=37 lang=cpp
 *
 * {37} Sudoku Solver
 */
#include <bit>
#include <chrono>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
// @lc code=start
class Solution {
   public:
    vector<vector<int>> bitmap;
    int reCnt;

    Solution() : bitmap(3, vector<int>(9, 0)), reCnt(0) {}

    void solveSudoku(vector<vector<char>>& board) {
        // convert to number board and flagging
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;

                int k = (i / 3) * 3 + j / 3;
                int v = board[i][j] - '0';
                flag(i, j, k, v);
            }
        }

        backtracking(board, 0, 0);
    }

    bool backtracking(vector<vector<char>>& board, int i, int j) {
        reCnt++;
        if (i == 9) return true;
        if (j == 9) return backtracking(board, i + 1, 0);
        if (board[i][j] != '.') return backtracking(board, i, j + 1);

        int k = (i / 3) * 3 + j / 3;
        for (char v = 1; v <= 9; ++v) {
            if (!checkValid(i, j, k, v)) continue;

            board[i][j] = '0' + v;
            flag(i, j, k, v);
            if (backtracking(board, i, j + 1)) return true;
            unflag(i, j, k, v);
        }
        board[i][j] = '.';
        return false;
    }

    bool checkFinish() {
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (bitmap[i][j] < 9) return false;
            }
        }
        return true;
    }

    bool checkValid(int i, int j, int k, int val) {
        int t = bitmap[0][i] | bitmap[1][j] | bitmap[2][k];
        return (t & (1 << val)) == 0;
    }

    void flag(int i, int j, int k, int val) {
        int t = 1 << val;
        bitmap[0][i] |= t;
        bitmap[1][j] |= t;
        bitmap[2][k] |= t;
    }

    void unflag(int i, int j, int k, int val) {
        int t = ~(1 << val);
        bitmap[0][i] &= t;
        bitmap[1][j] &= t;
        bitmap[2][k] &= t;
    }

    void printBoard(const vector<vector<char>>& board) {
        for (const auto& row : board) {
            for (const auto& cell : row) {
                cout << cell << ' ';
            }
            cout << endl;
        }
    }

    void bin(long n) {
        long i;
        cout << "0";
        for (i = 1 << 30; i > 0; i = i / 2) {
            if ((n & i) != 0) {
                cout << "1";
            } else {
                cout << "0";
            }
        }
        cout << endl;
    }
};
// @lc code=end
int main() {
    vector<vector<char>> board{
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

    auto start = chrono::high_resolution_clock::now();

    Solution sl;
    sl.bin(100);
    sl.solveSudoku(board);

    auto end = chrono::high_resolution_clock::now();
    double took = chrono::duration_cast<chrono::nanoseconds>(end - start).count();

    sl.printBoard(board);
    cout << "number of recursive calls: " << sl.reCnt << endl;
    cout << "took : " << took*1e-6 << " ns" << endl;
}
