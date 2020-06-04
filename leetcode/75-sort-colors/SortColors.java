import java.util.Arrays;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class SortColors {

    public void sortColors(int[] nums) {
        int i = 0, k = 0;
        while (i < nums.length && k < 3) {
            if (nums[i] == k) {
                i++;
                continue;
            }
            int j = i;
            while (++j < nums.length) {
                if (nums[j] == k) {
                    int t = nums[i];
                    nums[i] = nums[j];
                    nums[j] = t;
                    i += 1;
                }
            }
            k += 1;
        }
    }

    public static void main(String[] args) {
        int[] input = new int[]{0, 2, 0, 2, 1, 1, 0};
        new SortColors().sortColors(input);
        System.out.println(Arrays.toString(input));
    }
}
