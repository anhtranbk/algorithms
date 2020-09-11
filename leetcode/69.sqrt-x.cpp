/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */
#include <iostream>

using namespace std;
// @lc code=start
class Solution {
   public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x == 1) return 1;

        int m, v, l = 1, r = x;
        while (l < r) {
            m = l + (r-l)/2;
            v = x / m;

            if (v == m) return m;
            if (v < m)
                r = m;
            else {
                if (x / (m + 1) < m + 1) return m;
                l = m + 1;
            }
        }
        return m;
    }

    // Newton solution
    int mySqrt2(int x) {
        if (x == 0) return 0;
        long i = x;
        while (i > x / i)
            i = (i + x / i) / 2;
        return (int)i;
    }
};
// @lc code=end
int main() {
    Solution sl;
    for (int i = 0; i < 40; ++i) {
        int ans = sl.mySqrt(i);
        cout << "=>" << i << " " << ans << endl;
    }
    return 0;
}