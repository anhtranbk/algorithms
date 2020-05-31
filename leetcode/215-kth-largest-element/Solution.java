class Solution {
    // Counting-sort solution
    public int findKthLargest(int[] nums, int k) {
        int t = 10000;
        int[] cnt = new int[2*t+1];
        for (int n : nums) {
            cnt[t+n] += 1;
        }
        
        k = nums.length - k;
        for (int i = 1; i < cnt.length; i++) {
            cnt[i] += cnt[i-1];
            if (cnt[i] > k) return i-t;
        }
        return 0;
    }
}
