/*
 * @lc app=leetcode id=155 lang=rust
 *
 * [155] Min Stack
 */

// @lc code=start
use std::cmp;

struct MyListNode {
    val: i32,
    min: i32,
    prev: Option<Box<MyListNode>>,
}

struct MinStack {
    tail: Option<Box<MyListNode>>,
}

impl MyListNode {
    fn new(val: i32, min: i32, prev: Box<MyListNode>) -> Self {
        Self {
            val: val,
            min: min,
            prev: Some(prev),
        }
    }

    fn new_empty(val: i32, min: i32) -> Self {
        Self {
            val: val,
            min: min,
            prev: None,
        }
    }
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
    fn new() -> Self {
        Self {
            tail: Some(Box::new(MyListNode::new_empty(0, i32::MAX as i32))),
        }
    }

    fn push(&mut self, val: i32) {
        let curr = self.tail.take().unwrap();
        let min = cmp::min(curr.min, val);
        let new = MyListNode::new(val, min, curr);

        self.tail = Some(Box::new(new));
    }

    fn pop(&mut self) {
        let curr = self.tail.take().unwrap();
        self.tail = curr.prev;
    }

    fn top(&self) -> i32 {
        self.tail.as_ref().unwrap().val
    }

    fn get_min(&self) -> i32 {
        self.tail.as_ref().unwrap().min
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
// @lc code=end
fn main() {
    let mut mst = MinStack::new();
    mst.push(3);
    println!("{} - {}", mst.get_min(), mst.top());

    mst.push(4);
    println!("{} - {}", mst.get_min(), mst.top());

    mst.push(1);
    println!("{} - {}", mst.get_min(), mst.top());

    mst.push(5);
    mst.pop();
    mst.pop();
    println!("{} - {}", mst.get_min(), mst.top());
}
