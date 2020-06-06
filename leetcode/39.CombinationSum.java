class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        Stack<Integer> stack = new Stack<>();
        List<List<Integer>> ans = new ArrayList<>();
        
        this.process(candidates, target, 0, stack, ans);
        return ans;
    }
    
    private void process(int[] candidates, int target, int idx,
                        Stack<Integer> stack, List<List<Integer>> ans) {
        for (int i = idx; i < candidates.length; i++) {
            target -= candidates[i];
            if (target < 0) break;
            
            stack.push(candidates[i]);
            if (target == 0) {
                ans.add(new ArrayList(stack));
            } else {
                this.process(candidates, target, i, stack, ans);
            }
            
            target += candidates[i];
            stack.pop();
        }
    }
}