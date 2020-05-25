class JumpGame {
    public boolean canJump(int[] nums) {
        if (nums.length < 2) {
            return true;
        }
        int lastCanJump = nums.length - 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] + i >= lastCanJump) {
                lastCanJump = i;
            }
        }
        return lastCanJump == 0;
    }
}