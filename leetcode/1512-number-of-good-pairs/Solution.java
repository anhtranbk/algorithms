class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int n : nums) {
            if (counts.get(n) == null) {
                counts.put(n, 1);
            } else {
                counts.put(n, counts.get(n) + 1);
            }
        }
        int ans = 0;
        for (int key : counts.keySet()) {
            int val = counts.get(key);
            if (val > 1) {
                ans += val*(val-1)/2;
            }
        }
        return ans;
    }
}