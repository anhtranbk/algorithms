/*
 * @lc app=leetcode id=432 lang=rust
 *
 * [432] All O`one Data Structure
 */

use std::{
    cell::{RefCell, RefMut},
    collections::{HashMap, HashSet},
    rc::Rc,
};

// @lc code=start
struct ListNode {
    right: Option<Rc<RefCell<ListNode>>>,
    left: Option<Rc<RefCell<ListNode>>>,
    cnt: u32,
    keys: HashSet<String>,
}

impl ListNode {
    fn new() -> Self {
        Self {
            right: Option::None,
            left: Option::None,
            cnt: u32::MAX,
            keys: HashSet::new(),
        }
    }
}

struct AllOne {
    m: HashMap<String, Rc<RefCell<ListNode>>>,
    head: Rc<RefCell<ListNode>>,
    tail: Rc<RefCell<ListNode>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {
    fn new() -> Self {
        let dummy = Rc::new(RefCell::new(ListNode::new()));
        Self {
            m: HashMap::new(),
            head: Rc::clone(&dummy),
            tail: Rc::clone(&dummy),
        }
    }

    fn inc(&mut self, key: String) {
        if !self.m.contains_key(&key) {
            // add a new node to the tail of the list
            let node = Rc::new(RefCell::new(ListNode {
                right: Option::None,
                left: Some(Rc::clone(&self.tail)),
                cnt: 1,
                keys: self.new_string_set(&key),
            }));

            // if new node is the right node of the current tail
            // curly bracket here to makesure borrowed varibale self.tail is returned back
            // to the upper scope after this block code ends
            {
                let mut tail = self.tail.borrow_mut();
                tail.right = Some(Rc::clone(&node));
            }

            self.m.insert(key, Rc::clone(&node));
            self.tail = Rc::clone(&node);

            return;
        }

        // remove the key from current bucket
        let curr = self.m.remove(&key).unwrap();
        let mut ref_curr = curr.borrow_mut();

        ref_curr.keys.remove(&key);

        let new_cnt = ref_curr.cnt + 1;

        // we need to to keep borrowed value from `curr`` live long to ensure `left` live as long as it
        let left = ref_curr.left.as_ref().unwrap();
        // if the left node is the needed bucket, add key to this node
        if left.borrow().cnt == new_cnt {
            left.borrow_mut().keys.insert(key.clone());
            self.m.insert(key, Rc::clone(&left));
        } else {
            // else create a new node between the left and curr nodes
            let new_node = Rc::new(RefCell::new(ListNode {
                right: Some(Rc::clone(&left)),
                left: Some(Rc::clone(&curr)),
                cnt: new_cnt,
                keys: self.new_string_set(&key),
            }));
            self.m.insert(key, Rc::clone(&new_node));

            // on-the-fly borrowing ends when the statement ends.
            left.borrow_mut().right = Some(Rc::clone(&new_node));
            ref_curr.left = Some(Rc::clone(&new_node));
        }

        if ref_curr.keys.is_empty() {
            self.remove_empty_bucket(ref_curr);
        }
    }

    fn dec(&mut self, key: String) {
        // remove key from the current bucket
        // finc new bucket
        //      found -> add to new bucket
        //      not found -> remove key from main map
        // It is guaranteed that key exists in the data structure before the decrement so we can unwrap here.
        let curr = self.m.remove(&key).unwrap();
        let mut ref_curr = curr.borrow_mut();

        ref_curr.keys.remove(&key);

        let new_count = ref_curr.cnt - 1;
        if new_count == 0 {
            if ref_curr.keys.is_empty() {
                self.remove_empty_bucket(ref_curr);
            }
            return;
        }

        match ref_curr.right.as_mut() {
            Some(right) => {
                // if the left node is the needed bucket, add key to this node
                if right.borrow().cnt == new_count {
                    right.borrow_mut().keys.insert(key.clone());
                    self.m.insert(key, Rc::clone(right));
                } else {
                    // else create a new node between the curr and right nodes
                    let new_node = Rc::new(RefCell::new(ListNode {
                        right: Some(Rc::clone(right)),
                        left: Some(Rc::clone(&curr)),
                        cnt: new_count,
                        keys: self.new_string_set(&key),
                    }));
                    self.m.insert(key, Rc::clone(&new_node));

                    ref_curr.right = Some(Rc::clone(&new_node));
                    right.borrow_mut().left = Some(Rc::clone(&new_node));
                }
            }
            None => {
                let new_node = Rc::new(RefCell::new(ListNode {
                    right: Option::None,
                    left: Some(Rc::clone(&curr)),
                    cnt: new_count,
                    keys: self.new_string_set(&key),
                }));
                self.m.insert(key, Rc::clone(&new_node));

                ref_curr.right = Some(Rc::clone(&new_node));
                self.tail = Rc::clone(&new_node);
            }
        };

        if ref_curr.keys.is_empty() {
            self.remove_empty_bucket(ref_curr);
        }
    }

    fn get_max_key(&self) -> String {
        match self.head.borrow().right {
            Some(ref right) => right.borrow().keys.iter().next().unwrap().clone(),
            None => "".to_string(),
        }
    }

    fn get_min_key(&self) -> String {
        match self.tail.borrow().keys.iter().next() {
            Some(key) => key.clone(),
            None => "".to_string(),
        }
    }

    fn new_string_set(&self, key: &String) -> HashSet<String> {
        let mut set = HashSet::new();
        set.insert(key.clone());

        set
    }

    // remove the node buckets whose key set is empty
    fn remove_empty_bucket(&mut self, node: RefMut<ListNode>) {
        let left = node.left.as_ref().unwrap();
        let mut ref_left = left.borrow_mut();

        match node.right.as_ref() {
            Some(right) => {
                ref_left.right = Some(Rc::clone(&right));
                right.borrow_mut().left = Some(Rc::clone(&left));
            }
            None => {
                ref_left.right = Option::None;
                self.tail = Rc::clone(&left);
            }
        }
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne::new();
 * obj.inc(key);
 * obj.dec(key);
 * let ret_3: String = obj.get_max_key();
 * let ret_4: String = obj.get_min_key();
 */
// @lc code=end
fn main() {
    let mut obj = AllOne::new();
    obj.inc("a".to_string());
    obj.inc("a".to_string());
    obj.inc("a".to_string());
    obj.inc("b".to_string());
    obj.inc("b".to_string());
    obj.inc("c".to_string());
    println!("max: {}, min: {}", obj.get_max_key(), obj.get_min_key());

    obj.dec("a".to_string());
    obj.dec("a".to_string());
    obj.dec("c".to_string());
    println!("max: {}, min: {}", obj.get_max_key(), obj.get_min_key());
}
