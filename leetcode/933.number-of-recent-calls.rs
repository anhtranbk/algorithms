/*
 * @lc app=leetcode id=933 lang=rust
 *
 * [933] Number of Recent Calls
 */

// @lc code=start
use std::collections::VecDeque;


struct RecentCounter {
    nums: VecDeque<i32> 
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RecentCounter {

    fn new() -> Self {
        Self {
            nums: VecDeque::new(),
        }
    }
    
    fn ping(&mut self, t: i32) -> i32 {
        self.nums.push_back(t);

        while let Some(n) = self.nums.front() {
            if t-*n <= 3000 { break }
            self.nums.pop_front();
        }

        self.nums.len() as i32
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */
// @lc code=end
fn main () {
    let obj = RecentCounter::new();
    let re1 = obj.ping(100);
    let re2 = obj.ping(999);
    let re3 = obj.ping(4000);

    println!("{re1}, {re2}, {re3}")
}
