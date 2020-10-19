/*
 * @lc app=leetcode id=8 lang=cpp
 *
 * [8] String to Integer (atoi)
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        // ignore leading spaces
        while (i < s.length() && s[i] == ' ') i++;
        if (i == s.length()) return 0;

        // read the sign
        int sign = 1;
        if (s[i] == '-' || s[i] == '+') {
            if (s[i] == '-') sign = -1;
            i++;
        }

        // ignore leading zero characters
        while (i < s.length() && s[i] == '0') i++;
        if (i == s.length()) return 0;

        int ans = 0, cnt = 1;
        for (; i < s.length(); ++i) {
            int n = s[i] - '0';
            if (n < 0 || n > 9) break;

            if (cnt > 10) {
                return sign > 0 ? INT_MAX : INT_MIN;
            } else if (cnt == 10) {
                if (INT_MAX/10 < ans || (INT_MAX/10 == ans && n > INT_MAX%10)) {
                    return sign > 0 ? INT_MAX : INT_MIN;
                }
            }
            ans = ans*10 + n;
            cnt++;
        }
        return sign * ans;
    }
};

// @lc code=end
class TrivialSolution {
public:
    bool isOutOfRange(const vector<int>& digits, int sign) {
        if (digits.size() > 10) {
            return true;
        }
        if (digits.size() == 10) {
            vector<int> to_verify = {2,1,4,7,4,8,3,6,4};
            for (int i = 0; i < 9; ++i) {
                if (digits[i] < to_verify[i]) return false;
                else if (digits[i] > to_verify[i]) return true;
            }
            // brilliant checks here to return immediately if we found boundary
            if (sign > 0 && digits[9] >= 7) return true;
            else if (sign < 0 && digits[9] >= 8) return true;
        }
        return false;
    }

    int myAtoi(string s) {
        int i = 0;
        // ignore leading spaces
        while (i < s.length() && s[i] == ' ') i++;
        if (i == s.length()) return 0;

        // read the sign
        int sign = 1;
        if (s[i] == '-' || s[i] == '+') {
            if (s[i] == '-') sign = -1;
            i++;
        }

        // ignore leading zero characters
        while (i < s.length() && s[i] == '0') i++;
        if (i == s.length()) return 0;

        //  2147483647
        // -2147483648
        vector<int> digits;
        while (i++ < s.length() && digits.size() < 10) {
            int n = s[i] - '0';
            if (n < 0 || n > 9) break;
            digits.push_back(n);
        }
        if (digits.empty()) return 0;

        // verify out of range
        if (isOutOfRange(digits, sign)) {
            return sign > 0 ? 2147483647 : -2147483648;
        }

        int ans = 0;
        int base = 1;
        for (i = (int) digits.size() - 1; i > 0; --i) {
            ans += base * digits[i];
            base *= 10;
        }

        return sign * (ans + base * digits[0]);
    }
};

int main() {
    Solution sl;
    cout << sl.myAtoi(" -4325 bac") << endl;
    cout << sl.myAtoi(" -2147483648 bac") << endl;
    cout << sl.myAtoi(" 2147483647 bac") << endl;
    cout << sl.myAtoi("1175109307q7") << endl;
    cout << sl.myAtoi("-91283472332") << endl;
    cout << sl.myAtoi("21474836460") << endl;
}

