package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class JumpGame {

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

    public boolean bestSolution(int[] nums) {
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] == 0) {
                int j = 1;
                while (i-j >= 0 && nums[i-j] <= j) {
                    j++;
                }
                if (i-j == -1) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        JumpGame jumpGame = new JumpGame();
        System.out.println(jumpGame.canJump(new int[]{2, 3, 1, 1, 4}));
        System.out.println(jumpGame.canJump(new int[]{3, 2, 1, 0, 4}));
    }
}
