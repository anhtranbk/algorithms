package sieunhan.algorithm.leetcode;

import java.util.Arrays;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class JumpGame2 {

    public int jump(int[] nums) {
        return oN2Solution(nums);
    }

    private int oNSolution(int[] nums) {
        int[] steps = new int[nums.length];
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] + i >= nums.length - 1) {
                steps[i] = 1;
                continue;
            }

            int minHere = Integer.MAX_VALUE;
            for (int j = nums[i]; j >= 1; --j) {
                int step = steps[i + j] + 1;
                if (step > 0 && step < minHere) {
                    minHere = step;
                }
            }
            steps[i] = minHere;
        }
        System.out.println(Arrays.toString(steps));
        return steps[0];
    }

    private int oN2Solution(int[] nums) {
        int[] steps = new int[nums.length];
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] + i >= nums.length - 1) {
                steps[i] = 1;
                continue;
            }

            int minHere = Integer.MAX_VALUE;
            for (int j = nums[i]; j >= 1; --j) {
                int step = steps[i + j] + 1;
                if (step > 0 && step < minHere) {
                    minHere = step;
                }
            }
            steps[i] = minHere;
        }
        System.out.println(Arrays.toString(steps));
        return steps[0];
    }

    public static void main(String[] args) {
        JumpGame2 jumpGame2 = new JumpGame2();
//        System.out.println(jumpGame2.jump(new int[]{2, 3, 1, 1, 4}));
//        System.out.println(jumpGame2.jump(new int[]{1, 2, 3}));
        System.out.println(jumpGame2.jump(new int[]{2, 3, 0, 1, 4}));
    }
}
