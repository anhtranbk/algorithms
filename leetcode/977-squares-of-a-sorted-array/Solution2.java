class Solution {
    private static int sqr(int n) {
        return n*n;
    }
    
    public int[] sortedSquares(int[] nums) {
        int i = 0;
        while (i < nums.length && nums[i] < 0) i++;
        
        int j = i--, k = 0;
        int[] ans = new int[nums.length];
        
        while (i >= 0 && j < nums.length) {
            if (Math.abs(nums[i]) > Math.abs(nums[j])) {
                ans[k++] = sqr(nums[j]);
                j += 1;
            } else {
                ans[k++] = sqr(nums[i]);
                i -= 1;
            }
        }
        while (i >= 0) 
            ans[k++] = sqr(nums[i--]);
        while (j < nums.length) 
            ans[k++] = sqr(nums[j++]);
        
        return ans;
    }
}
