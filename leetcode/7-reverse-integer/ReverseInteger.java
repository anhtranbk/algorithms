package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class ReverseInteger {

    public int reverse(int x) {
        if (x == Integer.MIN_VALUE) return 0;
        int xAbs = Math.abs(x);

        long rev = 0;
        while (xAbs > 0) {
            int val = xAbs % 10;
            rev = rev * 10 + val;
            if (rev > Integer.MAX_VALUE) return 0;
            xAbs /= 10;
        }
        int n = (int) rev;
        return x > 0 ? n : -n;
    }

    // Seems it's acctually my own solution
    public int reverseOrigin(int x) {
        if (x == Integer.MIN_VALUE) return 0;
        int xAbs = Math.abs(x);

        int[] digits = new int[16];
        int d = 1;
        int i = 0;
        while (xAbs/d > 0) {
            int val = (xAbs / d) % 10;
            digits[i++] = val;
            if (d == 1000000000) break; // avoid overflow
            d = d * 10;
        }
        int n = 0;
        for (int j = 0; j < digits.length; j++) {
            double val = digits[j] * Math.pow(10, i-j-1) + n;
            if (val > Integer.MAX_VALUE) return 0;
            n = (int) val;
        }
        return x > 0 ? n : -n;
    }

    public static void main(String[] args) {
        System.out.println(new ReverseInteger().reverse(-2147483412));
    }
}
