/*
 * @lc app=leetcode id=109 lang=golang
 *
 * [109] Convert Sorted List to Binary Search Tree
 */
package leetcode

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func getSize(head *ListNode) int {
	size := 0
	for node := head; node != nil; node = node.Next {
		size += 1
	}
	return size
}

func getHeight(size int) int {
	h := 0
	for ; size > 0; size /= 2 {
		h += 1
	}
	return h
}

func buildTreeNodeON(
	depth int,
	height int,
	lnode *ListNode,
) (*TreeNode, *ListNode) {
	if lnode == nil {
		return nil, nil
	}
	if depth == height {
		return &TreeNode{
			Val:   lnode.Val,
			Left:  nil,
			Right: nil,
		}, lnode.Next
	}

	// build left node
	var left *TreeNode = nil
	if lnode.Next != nil {
		left, lnode = buildTreeNodeON(depth+1, height, lnode)
	}
	// set current list node value for current tree node
	tnode := &TreeNode{
		Val:   lnode.Val,
		Left:  left,
		Right: nil,
	}
	// build right node
	right, lnode := buildTreeNodeON(depth+1, height, lnode.Next)
	tnode.Right = right

	return tnode, lnode
}

func buildTreeNodeOlogN(lnode *ListNode) *TreeNode {
	if lnode == nil {
		return nil
	}
	if lnode.Next == nil {
		return &TreeNode{Val: lnode.Val}
	}

	// fast node start with one more step in order to allow our loop stop before mid element
	slow, fast := lnode, lnode.Next.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	mid := slow.Next
	slow.Next = nil
	tnode := &TreeNode{
		Val:   mid.Val,
		Left:  buildTreeNodeOlogN(lnode),
		Right: buildTreeNodeOlogN(mid.Next),
	}
	return tnode
}

func sortedListToBST(head *ListNode) *TreeNode {
	h := getHeight(getSize(head))
	if h == 0 {
		return nil
	}

	// tnode, _ := buildTreeNodeON(1, h, head)
	// return tnode

	return buildTreeNodeOlogN(head)
}

// @lc code=end
func buildListNode(nums []int) *ListNode {
	dummy := &ListNode{}
	curr := dummy
	for _, n := range nums {
		node := &ListNode{
			Val: n,
		}
		curr.Next = node
		curr = node
	}
	return dummy.Next
}

func enqueue(q []*TreeNode, n *TreeNode) []*TreeNode {
	return append(q, n)
}

func dequeue(q []*TreeNode) (*TreeNode, []*TreeNode) {
	return q[0], q[1:]
}

func printTreeNodePretty(node *TreeNode) {
	q := make([]*TreeNode, 0, 10)
	q = enqueue(q, node)
	for len(q) > 0 {
		v, nq := dequeue(q)
		fmt.Print(v.Val, " ")

		if v.Left != nil {
			nq = enqueue(nq, v.Left)
		}
		if v.Right != nil {
			nq = enqueue(nq, v.Right)
		}
		q = nq
	}
	fmt.Println()
}

func printTreeNodePreOrder(node *TreeNode) {
	if node == nil {
		return
	}
	fmt.Print(node.Val, " ")
	if node.Left != nil {
		printTreeNodePreOrder(node.Left)
	}
	if node.Right != nil {
		printTreeNodePreOrder(node.Right)
	}
}

func printListNode(node *ListNode) {
	for ; node != nil; node = node.Next {
		fmt.Print(node.Val, " ")
	}
	fmt.Println()
}

func Test109() {
	head := buildListNode([]int{-10, -3, 0, 5, 9})
	head = buildListNode([]int{1, 2, 3, 4, 5, 6, 7})
	printListNode(head)
	// one possible answer: [0,-3,9,-10,null,5]
	// 			0
	//   -3	   		9
	// -10 nil   5
	tnode := sortedListToBST(head)
	printTreeNodePretty(tnode)
	printTreeNodePreOrder(tnode)
}
