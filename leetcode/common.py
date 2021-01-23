from sys import exc_info
import unittest
from typing import List, Any, Optional, Dict, Tuple, Set
from queue import Queue

class BaseTestCase(unittest.TestCase):
    def assertArrayEquals(self, 
        expected: List[Any], 
        actual: List[Any], 
        sorted_before_comparing=False, 
        print_exec_info=True
    ):
        self.assertEqual(len(expected), len(actual))

        if sorted_before_comparing:
            expected = sorted(expected)
            actual = sorted(actual)

        for i in range(0, len(expected)):
            try:
                self.assertEqual(expected[i], actual[i])
            except Exception:
                if print_exec_info:
                    print('Exception when asserting at element ' + str(i))
                    print('Expected', expected)
                    print('Actual  ', actual)
                raise

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def vals_as_array(self) -> List[int]:
        arr = []
        node = self
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def __str__(self) -> str:
        node = self
        s = ''
        while node:
            s += str(node.val) + ('->' if node.next else '')
            node = node.next
        return s


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

        
def deserialize_tree(string) -> Optional[TreeNode]:
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root
    
    
def height(root: Optional[TreeNode]):
    return 1 + max(height(root.left), height(root.right)) if root else -1


def draw_node_ascii(node: Optional[TreeNode], w: int):
    s = str(node.val) if node else '.'
    sign = 1
    while len(s) < w:
        if sign > 0:
            s += ' '
        else:
            s = ' ' + s
        sign *= -1
    print(s, end='')


def draw_tree_ascii(root: Optional[TreeNode], leaf_width: int):
    h = height(root)
    max_width = pow(2, h) * leaf_width 
    if h > 6:
        raise ValueError("Do not support draw tree with heigh greater than 6: actual value is %d" % h)

    q: Queue[Tuple[TreeNode, int]] = Queue()
    q.put((root, 0))
    cur_lvl = 0
    
    while not q.empty():
        node, lvl = q.get()
        if lvl > h:
            break
        elif lvl > cur_lvl:
            cur_lvl = lvl
            print()
        
        w = max_width // pow(2, lvl)      
        draw_node_ascii(node, w) 

        q.put((node.left if node else None, lvl+1))
        q.put((node.right if node else None, lvl+1))

    print()

def find_in_bst(root: TreeNode, val: int) -> Optional[TreeNode]:
    node = root
    while node:
        if node.val == val:
            return node
        elif node.val < val:
            node = node.right
        else:
            node = node.left
    return None

def find_in_binary_tree(root: TreeNode, val: int) -> Optional[TreeNode]:
    if root.val == val:
        return root
    if root.left:
        node = find_in_binary_tree(root.left, val)
        if node:
            return node
    if root.right:
        node = find_in_binary_tree(root.right, val)
        if node:
            return node
    return None


if __name__ == "__main__":
    s = '[1,2,3,4,null,2,4,null,null,4]'
    root = deserialize_tree(s)
    draw_tree_ascii(root, leaf_width=2)