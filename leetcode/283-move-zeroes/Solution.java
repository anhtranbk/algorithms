class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0, j = 1;
        while (j < nums.length) {
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

    public void moveZeroes(int[] nums) {
        for (int i = 0, last = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int tmp = nums[i];
                nums[i] = nums[last];
                nums[last] = tmp;
                last++;
            }
        }
    }
}
