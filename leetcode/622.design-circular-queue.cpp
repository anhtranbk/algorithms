/*
 * @lc app=leetcode id=622 lang=cpp
 *
 * [622] Design Circular Queue
 */

// @lc code=start
class MyCircularQueue {
private:
    vector<int> nums;
public:
    MyCircularQueue(int k) : nums(k) {
    }
    
    bool enQueue(int value) {
        return false;    
    }
    
    bool deQueue() {
        return false; 
    }
    
    int Front() {
        return 0; 
    }
    
    int Rear() {
        return 0; 
    }
    
    bool isEmpty() {
        return false; 
    }
    
    bool isFull() {
        return false; 
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
// @lc code=end

