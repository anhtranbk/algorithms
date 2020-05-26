package sieunhan.algorithm.leetcode;

import java.util.Arrays;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class LeetCode34 {

    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0)
            return new int[]{-1, -1};
        
        int lo = 0, hi = nums.length - 1, mid = 0;
        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (target > nums[mid])
                lo = mid + 1;
            else if (target < nums[mid])
                hi = mid - 1;
            else break;
        }
        if (nums[mid] != target) return new int[]{-1, -1};

        int l = lo, r = mid, m = 0;
        while (l < r) {
            m = l + (r - l) / 2;
            if (target == nums[m]) r = m;
            else l = m + 1;
        }
        int first = l;

        l = mid;
        r = hi;
        while (l < r) {
            m = r - (r - l) / 2;
            if (target == nums[m]) l = m;
            else r = m - 1;
        }
        int last = r;

        return new int[]{first, last};
    }

    public static void main(String[] args) {
        int[] nums = new int[]{5, 7, 7, 8, 8, 10};
        int[] ans = new LeetCode34().searchRange(nums, 8);
        System.out.println(Arrays.toString(ans));
    }
}
