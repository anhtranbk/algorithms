
/*
 * @lc app=leetcode id=380 lang=golang
 *
 * [380] Insert Delete GetRandom O(1)
 */
package leetcode

import (
	"fmt"
	"math/rand"
)

// @lc code=start
type RandomizedSet struct {
	pos  map[int]int
	vals []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		pos:  make(map[int]int, 0),
		vals: make([]int, 0),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.pos[val]; ok {
		return false
	}
	this.pos[val] = len(this.vals)
	this.vals = append(this.vals, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	i, ok := this.pos[val]
	if !ok {
		return false
	}

	l := len(this.vals) - 1
	if i < l { // swap
		this.vals[i], this.vals[l] = this.vals[l], this.vals[i]
		this.pos[this.vals[i]] = i
	}

	this.vals = this.vals[:l]
	delete(this.pos, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	i := rand.Intn(len(this.vals))
	return this.vals[i]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
// @lc code=end
func Test380() {
	set := Constructor()
	set.Insert(0)
	fmt.Println(set.vals, set.pos)
	set.Insert(1)
	fmt.Println(set.vals, set.pos)
	set.Remove(0)
	fmt.Println(set.vals, set.pos)
	set.Insert(2)
	fmt.Println(set.vals, set.pos)
	set.Remove(1)
	fmt.Println(set.vals, set.pos)
	fmt.Println(set.GetRandom())
}
