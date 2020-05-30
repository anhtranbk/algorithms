#
# @lc app=leetcode id=146 lang=python3
#
# [110] LRU Cache
#

# @lc code=start
# Definition for a binary tree node.
class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.data = dict()

    def moveToTail(self, node: ListNode):
        if not node.next:
            return
        # swap value of current node and next node
        node.val, node.next.val = node.next.val, node.val
        node.key, node.next.key = node.next.key, node.key

        # swap ref in data map
        self.data[node.key] = node
        self.data[node.next.key] = node.next

        if self.tail == node.next:
            return

        # move node next to tail
        self.tail.next = node.next
        self.tail = self.tail.next

        node.next = node.next.next
        self.tail.next = None

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if not node:
            return -1

        val = node.val
        self.moveToTail(node)
        return val

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node:
            node.val = value
            self.moveToTail(node)
            return

        node = ListNode(key, value)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.data[key] = node

        if len(self.data) > self.capacity:
            tmp = self.head
            self.head = self.head.next
            del self.data[tmp.key]

    def print_list(self):
        node = self.head
        while node:
            print('({}:{})'.format(node.key, node.val), end='->' if node.next else '')
            node = node.next
        print()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end
if __name__ == '__main__':
    cache = LRUCache(capacity=5)
    cache.put(3, 3)
    cache.print_list()
    cache.put(1, 3)
    cache.print_list()
    cache.put(2, 3)
    cache.print_list()

    cache.put(1, 3)
    cache.print_list()
    cache.put(2, 3)
    cache.print_list()
    cache.put(3, 3)
    cache.print_list()

    cache.put(4, 3)
    cache.print_list()
    cache.put(5, 3)
    cache.print_list()
    cache.put(6, 3)
    cache.print_list()

