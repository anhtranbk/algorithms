/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class MinimumSubArraySum {

    public int minSubArrayLen(int s, int[] nums) {
        return solution2(s, nums);
    }

    /**
     * Prefix sum + Binary search approach
     * O(nlogN) solution
     */
    public int solution1(int s, int[] nums) {
        int[] sums = new int[nums.length + 1];
        for (int i = 1; i < sums.length; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }

        int ret = sums.length;
        for (int i = 0; i < sums.length; i++) {
            int len = findMinLength(sums, i, sums.length - 1, s);
            if (len < ret && len > 0) ret = len;
        }
        return ret < sums.length ? ret : 0;
    }

    int findMinLength(int[] sums, int lo, int hi, int s) {
        int t = lo;
        while (lo < hi) {
            int m = lo + (hi - lo) / 2;
            int k = sums[m] - sums[t];
            if (k < s) lo = m + 1;
            else if (k > s) hi = m;
            else return m - t;
        }
        return sums[lo] - sums[t] >= s ? lo - t : 0;
    }

    /**
     * Two pointer + sliding window approach
     * O(n) solution
     */
    public int solution2(int s, int[] nums) {
        int i = 0, j = 0, sum = 0, ret = Integer.MAX_VALUE;
        while (j < nums.length) {
            sum += nums[j];
            while (sum >= s) {
                ret = Math.min(ret, j - i + 1);
                sum -= nums[i++];
            }
            j += 1;
        }
        return ret < Integer.MAX_VALUE ? ret : 0;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2, 3, 1, 2, 4, 3};
        int[] nums2 = new int[]{1, 2, 3, 4, 5};

//        System.out.println(new MinimumSubArraySum().solution1(7, nums));
        System.out.println(new MinimumSubArraySum().solution2(15, nums2));
    }
}
