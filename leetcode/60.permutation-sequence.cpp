/*
 * @lc app=leetcode id=60 lang=cpp
 *
 * [60] Permutation Sequence
 */
#include <iostream>
#include <string>

using namespace std;
// @lc code=start
class Solution {
   public:
    string getPermutation(int n, int k) {
        vector<int> fact = factorial(n);
        vector<int> visited(n+1, 0);
        string ans("");

        int p;
        k--; // too brilliant
        for (int i = n-1; i >= 0; --i) {
            p = k / fact[i];
            k = k % fact[i];

            int v = nextAvailable(visited, n, p);
            ans = ans.append(to_string(v));
            visited[v] = 1;
        }

        return ans;
    }

    int nextAvailable(const vector<int>& visited, int n, int p) {
        for (int i = 1; i <= n; ++i) {
            if (visited[i] == 1) continue;
            if (--p < 0) return i;
        }
        return -1;
    }

    vector<int> factorial(int n) {
        vector<int> fact(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            fact[i] = i * fact[i - 1];
        }
        return fact;
    }
};
// @lc code=end
int main() {
    Solution sl;
    cout << sl.getPermutation(3, 3) << endl;
    cout << sl.getPermutation(3, 2) << endl;
    cout << sl.getPermutation(3, 4) << endl;
    cout << sl.getPermutation(3, 6) << endl;
    cout << sl.getPermutation(4, 6) << endl;
    cout << sl.getPermutation(4, 7) << endl;
    cout << sl.getPermutation(4, 8) << endl;
    cout << sl.getPermutation(4, 9) << endl;
    cout << sl.getPermutation(3, 1) << endl;
}
