class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        for i in range(index):
            if not node:
                break
            node = node.next
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended
        to the end of linked list. If index is greater than the length, the node
        will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for i in range(0, index - 1):
            if not curr:
                return
            curr = curr.next

        node = ListNode(val)
        node.next = curr.next
        curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for i in range(1, index):
            if not curr:
                return
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def print_list(self):
        node = self.head
        while node:
            print(node.val, end='->' if node.next else '')
            node = node.next
        print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == '__main__':
    mll = MyLinkedList()
    mll.addAtHead(1)
    mll.print_list()

    mll.addAtTail(3)
    mll.print_list()

    mll.addAtIndex(1, 2)
    mll.print_list()

    print(mll.get(1))

    mll.deleteAtIndex(1)
    print(mll.get(1))
