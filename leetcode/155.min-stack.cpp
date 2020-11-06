/*
 * @lc app=leetcode id=155 lang=cpp
 *
 * [155] Min Stack
 */

// @lc code=start
#include <limits.h>
#include <algorithm>

struct MyListNode
{
    int min;
    int val;
    MyListNode *prev;

    MyListNode(int min, int val) : MyListNode(min, val, nullptr) {}

    MyListNode(int min, int val, MyListNode *prev): min(min), val(val), prev(prev) {}
    {
    }
};

class MinStack
{
public:
    MyListNode *tail;

    MinStack()
    {
        this->tail = new MyListNode(INT_MAX, 0);
    }

    void push(int val)
    {
        int newMin = std::min(this->tail->min, val);
        MyListNode *tmp = new MyListNode(newMin, val, this->tail);
        this->tail = tmp;
    }

    void pop()
    {
        MyListNode *curr = this->tail;
        this->tail = this->tail->prev;
        delete curr;
    }

    int top()
    {
        return this->tail->val;
    }

    int getMin()
    {
        return this->tail->min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end
