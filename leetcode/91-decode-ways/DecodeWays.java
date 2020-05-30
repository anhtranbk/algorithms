//
// @lc app=leetcode id=91 lang=Java
// 
// [91] Decode Ways
// 

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
 // @lc code=start
public class DecodeWays {

    public int numDecodings(String s) {
        if (s.isEmpty()) return 0;
        int[] ct = new int[s.length() + 1];

        ct[s.length()] = 1;
        ct[s.length() - 1] = s.charAt(s.length() - 1) == '0' ? 0 : 1;

        for (int i = s.length() - 2; i >= 0; i--) {
            char curr = s.charAt(i);
            char prev = s.charAt(i + 1);

            if (prev == '0' && (curr == '0' || curr > '2')) return 0;
            if (curr == '0') ct[i] = 0;
            else if (curr > '2' || (curr == '2' && prev > '6'))
                ct[i] = ct[i + 1];
            else
                ct[i] = ct[i + 1] + ct[i + 2];
        }
        return ct[0];
    }

    public static void main(String[] args) {
        String[] input = new String[]{"101", "10", "226", "2206", "206", "025", "230", "12", "212", "1212"};
        for (String s : input) System.out.println(new DecodeWays().numDecodings(s));
    }
}

// @lc code=end
