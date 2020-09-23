/*
 * @lc app=leetcode id=108 lang=golang
 *
 * [108] Convert Sorted Array to Binary Search Tree
 */
package leetcode

import "fmt"

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getNode(nums []int, from int, to int) *TreeNode {
	if from > to {
		return nil
	}
	mid := from + (to-from)/2
	root := &TreeNode{
		Val:   nums[mid],
		Left:  getNode(nums, from, mid-1),
		Right: getNode(nums, mid+1, to),
	}
	return root
}

func sortedArrayToBST(nums []int) *TreeNode {
	return getNode(nums, 0, len(nums)-1)
}

// @lc code=end
func Test108() {
	node := sortedArrayToBST([]int{-10, -3, 0, 5, 9})
	fmt.Println(node.Val, node.Left.Val, node.Right.Val)
}
