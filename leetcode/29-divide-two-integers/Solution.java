/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class DivideTwoInteger {

    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        if (divisor == 1) return dividend;
        if (divisor == -1) return -dividend;

        int dividendAbs = Math.abs(dividend);
        int divisorAbs = Math.abs(divisor);
        int count = dividePositive(dividendAbs, divisorAbs);

        return (dividend > 0 == divisor > 0) ? count : -count;
    }

    private int dividePositive(int dividend, int divisor) {
        int count = 0;
        int shift = 0;
        while (dividend - (divisor << shift) > 0) {
            shift++;
            count = count > 0 ? count + count : 1;
        }
        if (shift > 0) {
            dividend = dividend - (divisor << (shift - 1));
        }

        while (dividend - divisor >= 0) {
            count += 1;
            dividend = dividend - divisor;
        }
        return count;
    }

    private int dividePositiveBetter(int dividend, int divisor) {
        int count = 0;
        while (dividend - divisor >= 0) {
            int step = 1;
            int curr = divisor;
            while (dividend - (curr + curr) > 0 ) { // Curr + curr ( because it increment 2 times)
                curr = curr + curr;
                step += step;
            }

            count += step;
            dividend = dividend - curr; // Decrement Dividend
        }

        return count;
    }

    public static void main(String[] args) {
//        int dividend = Integer.parseInt(args[0]);
//        int divisor = Integer.parseInt(args[1]);
        System.out.println(new DivideTwoInteger().divide(10, -3));
    }
}
