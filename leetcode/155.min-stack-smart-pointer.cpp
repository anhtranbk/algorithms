/*
 * @lc app=leetcode id=155 lang=cpp
 *
 * [155] Min Stack
 */

// @lc code=start
#include <limits.h>
#include <algorithm>
#include <memory>
#include <iostream>

struct MyListNode
{
    int min;
    int val;
    std::unique_ptr<MyListNode> prev = std::make_unique<MyListNode>(nullptr);

    MyListNode(int min, int val) : min(min), val(val) {}

    MyListNode(int min, int val, std::unique_ptr<MyListNode>& prev): min(min), val(val) {
        this->prev = std::move(prev);
    }

    ~MyListNode() {
        std::cout << "MyListNode destroyed" << val << std::endl;
    }
};

class MinStack
{
public:
    std::unique_ptr<MyListNode> tail;

    MinStack()
    {
        this->tail = std::make_unique<MyListNode>(MyListNode(INT_MAX, 0));
    }

    void push(int val)
    {
        int newMin = std::min(this->tail->min, val);
        auto curr = std::move(this->tail);
        this->tail = std::make_unique<MyListNode>(MyListNode(newMin, val, curr));
    }

    void pop()
    {
        this->tail = std::move(this->tail->prev);
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
int main(int argc, char *argv[]) {
    MinStack stack;
    stack.push(1);
    stack.push(2);
    stack.pop();
}