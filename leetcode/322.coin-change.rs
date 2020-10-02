/*
 * @lc app=leetcode id=322 lang=rust
 *
 * [322] Coin Change
 */
struct Solution {}

// @lc code=start
impl Solution {
    pub fn coin_change(coins: Vec<i32>, n: i32) -> i32 {
        const INF: i32 = 10001;
        let n = n as usize;
        let mut dp = vec![INF; n + 1];

        dp[0] = 0;
        for i in 1..dp.len() {
            for c in coins.iter() {
                let j = (i as i32) - *c;
                if j >= 0 {
                    let j = j as usize;
                    dp[i] = std::cmp::min(dp[i], 1 + dp[j]);
                }
            }
        }

        if dp[n] >= INF {
            -1
        } else {
            dp[n]
        }
    }
}
// @lc code=end
#[cfg(test)]
mod tests {
    #[test]
    fn test_coin_change() {
        assert_eq!(super::coin_change(vec![1, 2, 5], 11), 3);
        assert_eq!(super::coin_change(vec![2, 3], 5), -1);
        assert_eq!(super::coin_change(vec![1], 0), 0);
    }
}

fn main() {
    let v1 = vec![1, 2, 5];
    let a1 = Solution::coin_change(v1, 11);

    println!("fucking result: {}", a1);
}
