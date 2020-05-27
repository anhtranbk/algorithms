/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class LastStoneWeight {

    public int lastStoneWeight(int[] stones) {
        int[] counts = new int[1001];
        for (int stone : stones) {
            counts[stone] += 1;
        }
        int i = 1000;
        while (i > 0) {
            if (counts[i] == 0) {
                i--;
                continue;
            }
            if (counts[i] > 1) counts[i] = counts[i] % 2;
            if (counts[i] > 0) {
                int j = i - 1;
                while (j > 0 && counts[j] == 0) j--;
                if (j <= 0) return i;
                counts[i] = 0;
                counts[j] -= 1;
                counts[i-j] += 1;
            }
            i--;
        }
        return counts[1];
    }

    public static void main(String[] args) {
        LastStoneWeight sol = new LastStoneWeight();
        System.out.println(sol.lastStoneWeight(new int[]{1,3}));
    }
}
