/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class PalindromeNumber {

    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int[] digits = new int[12];
        int d = 1;
        int i = 0;
        while (x/d > 0) {
            digits[i++] = (x/d) % 10;
            if (d == 1000000000) break; // avoid overflow
            d = d * 10;
        }
        for (int j = 0; j < i/2; j++) {
            if (digits[j] != digits[i-j-1]) return false;
        }
        return true;
    }

    // wrong answer
    public boolean isPalindrome2(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int rev = 0;
        while (x > rev) {
            int val = x % 10;
            rev = rev * 10 + val;
            x /= 10;
        }
        return x == rev || x == rev / 10;
    }

    public static void main(String[] args) {
        System.out.println(new PalindromeNumber().isPalindrome(300));
    }
}
