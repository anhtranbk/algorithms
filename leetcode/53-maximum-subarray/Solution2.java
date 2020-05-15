package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class MaxSubArray {

    public int maxSubArray(int[] nums) {
        return kadaneSolution(nums);
    }

    public int kadaneSolution(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            if (sum > maxSum) maxSum = sum;
            else if (sum < 0) sum = 0;
        }
        return maxSum;
    }

    public int bestSolution(int[] nums) {
        throw new UnsupportedOperationException();
    }

    public static void main(String[] args) {
        MaxSubArray maxSubArray = new MaxSubArray();
        int sum = maxSubArray.maxSubArray(new int[]{-2, -1, -3, -4, -1, -2, -1, -5, -4});
        System.out.println(sum);
    }
}
