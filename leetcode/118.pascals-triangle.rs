/*
 * @lc app=leetcode id=118 lang=rust
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let size = num_rows as usize;
        let mut v1 = vec![vec![1]];

        for i in 1..size {
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
        return v1;
    }
}
// @lc code=end
