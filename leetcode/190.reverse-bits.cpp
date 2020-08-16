/*
 * @lc app=leetcode id=190 lang=cpp
 *
 * [190] Reverse Bits
 */
#include <iostream>

using namespace std;

void bin(uint32_t n) {
    uint32_t i;
    for (i = 1 << 31; i > 0; i = i / 2) {
        if ((n & i) != 0) {
            cout << "1";
        } else {
            cout << "0";
        }
    }
    cout << endl;
}
// @lc code=start
class Solution {
   public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t v = 0;
        uint32_t mostLeft = 1 << 31;
        for (int i = 0; i < 16; i++) {
            uint32_t lmask = 1 << i;
            uint32_t rmask = mostLeft >> i;

            v |= ((lmask & n) << (31 - 2*i)); 
            v |= ((rmask & n) >> (31 - 2*i));
        }
        return v;
    }

    // https://leetcode.com/problems/reverse-bits/solutions/54741/o-1-bit-operation-c-solution-8ms/
    uint32_t reverseBits_2(uint32_t n) {
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
    }
};
// @lc code=end
int main() {
    Solution sl;
    cout << sl.reverseBits(45) << " " << sl.reverseBits_2(45) << endl; 
}