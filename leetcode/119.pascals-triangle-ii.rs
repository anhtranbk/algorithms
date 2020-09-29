/*
 * @lc app=leetcode id=119 lang=rust
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let size = row_index as usize;
        let mut v1 = vec![vec![1]];

        for i in 1..size+1 {
            let mut v2 = vec![1];
            for j in 1..i {
                let t = v1[i-1][j-1] + v1[i-1][j];
                v2.push(t);
            }
            if i > 0 {
                v2.push(1);
            } 
            v1.push(v2);
        }

        let mut ans: Vec<i32> = Vec::new();
        for (i, t) in v1[size].iter().enumerate() {
            ans.push(*t);
        }
        return ans;
    }
}
// @lc code=end

