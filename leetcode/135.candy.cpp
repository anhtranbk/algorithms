/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 */
#include <iostream>
// uncomment to disable assert()
// #define NDEBUG
#include <algorithm>
#include <cassert>
#include <stack>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
   public:
    // https://leetcode.com/problems/candy/solutions/42769/a-simple-solution/
    // two passes solution
    // O(N) time, O(N) space
    //  try to summarize the post's idea:
    // Do it in two directions.
    // The first loop makes sure children with a higher rating get more candy than its left neighbor; 
    // the second loop makes sure children with a higher rating get more candy than its right neighbor.
    int candy(vector<int> &ratings) {
        int size = ratings.size();
        if(size<=1)
            return size;
        vector<int> num(size,1);
        for (int i = 1; i < size; i++)
        {
            if(ratings[i]>ratings[i-1])
                num[i]=num[i-1]+1;
        }
        for (int i= size-1; i>0 ; i--)
        {
            if(ratings[i-1]>ratings[i])
                num[i-1]=max(num[i]+1,num[i-1]);
        }
        int result=0;
        for (int i = 0; i < size; i++)
        {
            result+=num[i];
        }
        return result;
        }

    int candy2(vector<int>& ratings) {
        if (ratings.empty()) return 0;
        if (ratings.size() == 1) return 1;

        int l = 0;
        int r = 1;
        int ans = 0;
        while (r < ratings.size()) {
            // find local minimum
            if (
                (r == ratings.size()-1) ||
                (ratings[r - 1] > ratings[r] && ratings[r] <= ratings[r + 1])
            ) {
                ans += populate(ratings, l, r);
                l = r+1;
            }
            r++;
        }

        return ans;
    }

    int populate(vector<int>& ratings, int l, int r) const { 
        int ans = 0; 
        int t1 = (l == 0 || ratings[l-1] == ratings[l]) ? 1 : 2;
        cout << "populate " << l << " " << r << " " << endl;
        while (l < ratings.size() && ratings[l] <= ratings[l + 1]) {
            ans += t1;
            cout << "add by t1 " << t1 << endl;
            t1 += ratings[l] < ratings[l+1] ? 1 : 0;
            l++;
        }

        int t2 = 1;
        while (r > 0 &&ratings[r - 1] > ratings[r]) {
            ans += t2;
            cout << "add by t2 " << t2 << endl;
            t2++;
            r--;
        }

        // add value for local peak
        return ans + max(t1, t2);
    }
};
// @lc code=end
int main() {
    Solution sl;

    vector<int> ratings1{1, 0, 2};
    int r1 = sl.candy(ratings1);
    cout << "r1 = " << r1 << endl;
    assert(5 == r1);

    vector<int> ratings2{1, 2, 2};
    int r2 = sl.candy(ratings2);
    cout << "r2 = " << r2 << endl;
    assert(4 == r2);

    vector<int> ratings3{1,3,2,2,1};
    int r3 = sl.candy(ratings3);
    cout << "r3 = " << r3 << endl;
    assert(7 == r3);
}