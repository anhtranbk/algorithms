package sieunhan.algorithm.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class HappyNumber {

    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while (true) {
            int s = 0;
            while (n > 0) {
                int d = n % 10;
                s += d*d;
                n /= 10;
            }
            System.out.println(s);
            if (s == 1) return true;
            if (!set.add(s)) {
                System.out.println(s + " repeated");
                return false;
            }
            n = s;
        }
    }

    public static void main(String[] args) {
        System.out.println(new HappyNumber().isHappy(32515));
    }
}
