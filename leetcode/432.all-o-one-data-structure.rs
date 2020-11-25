/*
 * @lc app=leetcode id=432 lang=rust
 *
 * [432] All O`one Data Structure
 */

// @lc code=start
use std::{
    cell::{RefCell, RefMut},
    collections::{HashMap, HashSet},
    rc::Rc,
};

struct BucketNode {
    right: Option<Rc<RefCell<BucketNode>>>,
    left: Option<Rc<RefCell<BucketNode>>>,
    cnt: u32,
    keys: HashSet<String>,
}

impl BucketNode {
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
    m: HashMap<String, Rc<RefCell<BucketNode>>>,
    head: Rc<RefCell<BucketNode>>,
    tail: Rc<RefCell<BucketNode>>,
}

fn single_set<T: Clone + std::cmp::Eq + std::hash::Hash>(key: &T) -> HashSet<T> {
    let mut set = HashSet::new();
    set.insert(key.clone());
    set
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {
    fn new() -> Self {
        let dummy = Rc::new(RefCell::new(BucketNode::new()));
        Self {
            m: HashMap::new(),
            head: Rc::clone(&dummy),
            tail: Rc::clone(&dummy),
        }
    }

    fn inc(&mut self, key: String) {
        if !self.m.contains_key(&key) {
            if self.tail.borrow().cnt == 1 {
                let tail = Rc::clone(&self.tail);
                self.add_key_to_bucket(tail, key);
            } else {
                // add a new node to the tail of the list
                self.append_to_last(1, key);
            }
            return;
        }

        // remove the key from current bucket
        let curr = self.m.remove(&key).unwrap();

        let (left, new_cnt) = {
            let mut ref_curr = curr.borrow_mut();
            ref_curr.keys.remove(&key);

            (Rc::clone(ref_curr.left.as_ref().unwrap()), ref_curr.cnt + 1)
        };

        // if the left node is the needed bucket, add key to this node
        if left.borrow().cnt == new_cnt {
            self.add_key_to_bucket(Rc::clone(&left), key);
        } else {
            let l = Rc::clone(&left);
            let r = Rc::clone(&curr);
            self.insert_new_node(new_cnt, key, l, r);
        }

        // re-create this variable as we want release prev variable to curr can be borrowed by self.insert_new_node func
        let ref_curr = curr.borrow_mut();
        if ref_curr.keys.is_empty() {
            self.remove_empty_bucket(ref_curr);
        }
    }

    fn dec(&mut self, key: String) {
        // It is guaranteed that key exists in the data structure before the decrement so we can unwrap here.
        let curr = self.m.remove(&key).unwrap();
        let mut ref_curr = curr.borrow_mut();

        ref_curr.keys.remove(&key);
        self.m.remove(&key);

        let new_cnt = ref_curr.cnt - 1;
        if new_cnt == 0 {
            if ref_curr.keys.is_empty() {
                self.remove_empty_bucket(ref_curr);
            }
            return;
        }

        match ref_curr.right.as_ref() {
            // borrow right from ref_curr
            Some(right) => {
                // if the left node is the needed bucket, add key to this node
                if right.borrow().cnt == new_cnt {
                    self.add_key_to_bucket(Rc::clone(&right), key);
                } else {
                    // else create a new node between the curr and right nodes
                    // clone here as we are borrowing right from curr, so we can not borrow more
                    let l = Rc::clone(&curr);
                    let r = Rc::clone(&right);
                    self.insert_new_node(new_cnt, key, l, r);
                }
            }
            None => {
                self.append_to_last(new_cnt, key);
            }
        }

        // println!("bucket {}, size {}", ref_curr.cnt, ref_curr.keys.len());
        if ref_curr.keys.is_empty() {
            self.remove_empty_bucket(ref_curr);
        }
    }

    fn get_max_key(&self) -> String {
        self.print_all();
        match self.head.borrow().right.as_ref() {
            Some(right) => right.borrow().keys.iter().next().unwrap().clone(),
            None => "".to_string(),
        }
    }

    fn get_min_key(&self) -> String {
        self.print_all();
        self.tail
            .borrow()
            .keys
            .iter()
            .next()
            .unwrap_or(&String::new())
            .clone()
    }

    fn print_all(&self) {
        let mut node = Rc::clone(&self.head);
        while node.borrow().right.is_some() {
            node = {
                let tmp = Rc::clone(node.borrow().right.as_ref().unwrap());
                tmp
            };
            println!(
                "bucket {}, size {}",
                node.borrow().cnt,
                node.borrow().keys.len()
            );
        }
    }

    // remove the node buckets whose key set is empty
    fn remove_empty_bucket(&mut self, node: RefMut<BucketNode>) {
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

    fn insert_new_node(
        &mut self,
        cnt: u32,
        key: String,
        left: Rc<RefCell<BucketNode>>,
        right: Rc<RefCell<BucketNode>>,
    ) {
        let new_node = Rc::new(RefCell::new(BucketNode {
            right: Some(Rc::clone(&left)),
            left: Some(Rc::clone(&right)),
            cnt,
            keys: single_set(&key),
        }));

        self.m.insert(key, Rc::clone(&new_node));

        right.borrow_mut().left = Some(Rc::clone(&new_node));
        left.borrow_mut().right = Some(Rc::clone(&new_node));
    }

    fn append_to_last(&mut self, cnt: u32, key: String) -> Rc<RefCell<BucketNode>> {
        let node = Rc::new(RefCell::new(BucketNode {
            right: Option::None,
            left: Some(Rc::clone(&self.tail)),
            cnt,
            keys: single_set(&key),
        }));
        self.tail.borrow_mut().right = Some(Rc::clone(&node));
        self.tail = Rc::clone(&node);
        self.m.insert(key, Rc::clone(&node));

        node
    }

    fn add_key_to_bucket(&mut self, node: Rc<RefCell<BucketNode>>, key: String) {
        node.borrow_mut().keys.insert(key.clone());
        self.m.insert(key, Rc::clone(&node));
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
