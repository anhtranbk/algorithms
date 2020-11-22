/*
 * @lc app=leetcode id=381 lang=rust
 *
 * [381] Insert Delete GetRandom O(1) - Duplicates allowed
 */

// @lc code=start
use std::collections::{HashMap, HashSet};

use rand::{rngs::ThreadRng, Rng};

struct RandomizedCollection {
    pos: HashMap<i32, HashSet<usize>>,
    vals: Vec<i32>,
    rnd: ThreadRng,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedCollection {
    fn new() -> Self {
        Self {
            pos: HashMap::new(),
            vals: Vec::new(),
            rnd: rand::thread_rng(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        self.vals.push(val);
        let len = self.vals.len() - 1;

        let mut not_present = true;
        match self.pos.get_mut(&val) {
            Some(set) => {
                not_present = set.is_empty();
                set.insert(len);
            }
            None => {
                let mut set = HashSet::new();
                set.insert(len);
                self.pos.insert(val, set);
            }
        }

        not_present
    }

    fn remove(&mut self, val: i32) -> bool {
        if !self.pos.contains_key(&val) {
            return false;
        }
        let set = self.pos.get_mut(&val).unwrap();
        if set.is_empty() {
            return false;
        }
        let idx = *set.iter().next().unwrap();
        set.take(&idx);

        // if the value at index idx is not the last element -> swap with the last element
        let last_idx = self.vals.len() - 1;
        if idx != last_idx {
            // remove index of the last element in HashMap `pos` add add new index
            let set = self.pos.get_mut(self.vals.get(last_idx).unwrap()).unwrap();
            set.remove(&last_idx);
            set.insert(idx);

            let tmp = self.vals[idx];
            self.vals[idx] = self.vals[last_idx];
            self.vals[last_idx] = tmp;
        }
        self.vals.pop();

        true
    }

    fn get_random(&mut self) -> i32 {
        let idx = self.rnd.gen_range(0..self.vals.len());
        return self.vals[idx];
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * let obj = RandomizedCollection::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
// @lc code=end
fn main() {
    let mut c = RandomizedCollection::new();
    println!("{}", c.insert(1));
    println!("{}", c.insert(2));
    println!("{}", c.insert(1));
    println!("{}", c.insert(3));
    println!("{}", c.insert(2));

    println!("{}", c.remove(2));
    println!("{}", c.remove(3));
    println!("{}", c.remove(3));

    println!("{}", c.get_random());
    println!("{}", c.get_random());
    println!("{}", c.get_random());
}
