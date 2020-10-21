/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */
#include <iostream>

using namespace std;

// @lc code=start
class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
        } 
        
        long num = labs(n);
        double pow = 1;
        
        while(num){ // equivalent to while(num != 0)
            if(num & 1) { // equivalent to if((num & 1) != 0)
                pow *= x;
            }
            x *= x;
            num >>= 1;
        }
        
        return pow;
    }
};
// @lc code=end
int main() {
    Solution sl;
    cout << sl.myPow(2.00000, 10) << endl;
    cout << sl.myPow(2.10000, 3) << endl;
    cout << sl.myPow(2.00000, -2) << endl;
    cout << sl.myPow(2.00000, -2147483647) << endl;
}

