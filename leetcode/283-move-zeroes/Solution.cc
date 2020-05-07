class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 1;
        while (j < nums.size()) {
            if (nums[j] == 0)
                j++;
            else if (j <= i)
                j = i + 1;
            else if (nums[i] != 0)
                i++;
            else {
                nums[i++] = nums[j];
                nums[j++] = 0;
            }
        }
    }
};