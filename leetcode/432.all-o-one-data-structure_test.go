/*
 * @lc app=leetcode id=432 lang=golang
 *
 * [432] All O`one Data Structure
 */
package leetcode

import (
	"encoding/json"
	"fmt"
	"testing"
)

// @lc code=start
type BucketNode struct {
	right *BucketNode
	left  *BucketNode
	cnt   uint32
	keys  map[string]struct{}
}

type AllOne struct {
	m    map[string]*BucketNode
	head *BucketNode
	tail *BucketNode
}

// rename it to Constructor before submitting to LeetCode
func Constructor() AllOne {
	dummy := BucketNode{
		cnt:  uint32(2<<31 - 1),
		keys: map[string]struct{}{},
	}
	return AllOne{
		m:    map[string]*BucketNode{},
		head: &dummy,
		tail: &dummy,
	}
}

func (this *AllOne) Inc(key string) {
	curr, ok := this.m[key]
	if !ok {
		if this.tail.cnt == 1 {
			this.addKeyToBucket(key, this.tail)
		} else {
			this.insertNodeToLast(1, key)
		}
		return
	}
	// remove the key from the current bucket
	delete(curr.keys, key)
	delete(this.m, key)

	// remove current bucket if it now doesn't contain any keys
	defer func() {
		if len(curr.keys) == 0 {
			this.removeEmptyBucket(curr)
		}
	}()

	// add the key to the next bucket
	left := curr.left
	if left.cnt == curr.cnt+1 {
		this.addKeyToBucket(key, left)
	} else {
		this.insertNode(left, curr, curr.cnt+1, key)
	}
}

func (this *AllOne) Dec(key string) {
	curr := this.m[key]
	// remove the key from the current bucket
	delete(curr.keys, key)
	delete(this.m, key)

	// remove current bucket if it now doesn't contain any keys
	defer func() {
		if len(curr.keys) == 0 {
			this.removeEmptyBucket(curr)
		}
	}()

	if curr.cnt-1 == 0 {
		return
	}

	right := curr.right
	if right == nil {
		this.insertNodeToLast(curr.cnt-1, key)
		return
	}

	if right.cnt == curr.cnt-1 {
		this.addKeyToBucket(key, right)
	} else {
		this.insertNode(curr, right, curr.cnt-1, key)
	}
}

func (this *AllOne) GetMaxKey() string {
	if this.head.right != nil {
		for k := range this.head.right.keys {
			return k
		}
	}
	 return ""
}

func (this *AllOne) GetMinKey() string {
	for k := range this.tail.keys {
		return k
	}
	return ""
}

func (this *AllOne) addKeyToBucket(key string, node *BucketNode) {
	node.keys[key] = struct{}{}
	this.m[key] = node
}

func (this *AllOne) insertNode(
	left *BucketNode,
	right *BucketNode,
	cnt uint32,
	key string,
) *BucketNode {
	node := &BucketNode{
		right: right,
		left:  left,
		cnt:   cnt,
		keys:  map[string]struct{}{key: struct{}{}},
	}
	left.right = node
	right.left = node
	this.m[key] = node
	return node
}

func (this *AllOne) removeEmptyBucket(node *BucketNode) {
	left := node.left
	if node.right != nil {
		// fmt.Printf("bucket %d between %d and %d removed\n", node.cnt, left.cnt, node.right.cnt)
		left.right = node.right
		node.right.left = left
	} else {
		if node.cnt > 9999 {
			fmt.Println("bucket removed from the last", node.cnt)
		}
		left.right = nil
		this.tail = left
	}
}

func (this *AllOne) insertNodeToLast(cnt uint32, key string) *BucketNode {
	node := &BucketNode{
		left: this.tail,
		cnt:  cnt,
		keys: map[string]struct{}{key: struct{}{}},
	}
	this.tail.right = node
	this.tail = node
	this.m[key] = node

	return node
}

/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */
// @lc code=end
func (this *AllOne) printAllKeys(fnName string) {
	fmt.Printf("-------------- %s -----------------\n", fnName)
	for node := this.head.right; node != nil; node = node.right {
		fmt.Println(node.cnt, node.keys)
	}
}

func TestLeetCode432(t *testing.T) {
	t.Run("my test", func(t *testing.T) {
		obj := Constructor()
		obj.Inc("a")
		obj.Inc("a")
		obj.Inc("a")
		obj.Inc("b")
		obj.Inc("b")
		obj.Inc("c")
		if obj.GetMaxKey() != "a" {
			t.Fatalf("expected %v, got %v", "a", obj.GetMaxKey())
		}
		if obj.GetMinKey() != "c" {
			t.Fatalf("expected %v, got %v", "c", obj.GetMinKey())
		}

		obj.Dec("a")
		obj.Dec("a")
		obj.Dec("c")
		if obj.GetMaxKey() != "b" {
			t.Fatalf("expected %v, got %v", "b", obj.GetMaxKey())
		}
		if obj.GetMinKey() != "a" {
			t.Fatalf("expected %v, got %v", "a", obj.GetMinKey())
		}
	})

	type tests struct {
		cmd  string
		args []string
		want string
	}

	parseTestArgs := func(in1, in2, out1 string) []tests {
		var arr []string
		json.Unmarshal([]byte(in1), &arr)
		tts := make([]tests, len(arr))
		for i, cmd := range arr {
			tts[i].cmd = cmd
		}

		var arr2 [][]string
		json.Unmarshal([]byte(in2), &arr2)
		for i, args := range arr2 {
			tts[i].args = args
		}

		arr = arr[:0]
		json.Unmarshal([]byte(out1), &arr)
		for i, o := range arr {
			tts[i].want = o
		}

		return tts
	}

	t.Run("leetcode test case 13", func(t *testing.T) {
		input_1 := `["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]`
		input_2 := `[[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]`
		output := `[null,null,null,null,null,"hello",null,null,null,null,null,null,null,"leet"]`

		tts := parseTestArgs(input_1, input_2, output)
		fmt.Println(tts)

		var obj AllOne
		for _, tt := range tts {
			switch tt.cmd {
			case "AllOne":
				obj = Constructor()
			case "inc":
				obj.Inc(tt.args[0])
				obj.printAllKeys("Inc " + tt.args[0])
			case "dec":
				obj.Dec(tt.args[0])
				obj.printAllKeys("Dec " + tt.args[0])
			case "getMaxKey":
				obj.printAllKeys("GetMaxKey")
				got := obj.GetMaxKey()
				if got != tt.want {
					t.Fatalf("expected %v, got %v", tt.want, got)
				}
			case "getMinKey":
				obj.printAllKeys("GetMinKey")
				got := obj.GetMinKey()
				if got != tt.want {
					t.Fatalf("expected %v, got %v", tt.want, got)
				}
			}
		}
	})

	t.Run("leetcode test case 19", func(t *testing.T) {
		input_1 := `["AllOne","inc","inc","inc","inc","inc","inc","dec","inc","dec","inc","dec","inc","dec","getMaxKey","getMinKey"]`
		input_2 := `[[],["a"],["a"],["a"],["a"],["a"],["b"],["b"],["b"],["b"],["b"],["b"],["b"],["b"],[],[]]`
		output := `[null,null,null,null,null,null,null,null,null,null,null,null,null,null,"a","a"]`

		tts := parseTestArgs(input_1, input_2, output)
		fmt.Println(tts)

		var obj AllOne
		for _, tt := range tts {
			switch tt.cmd {
			case "AllOne":
				obj = Constructor()
			case "inc":
				obj.Inc(tt.args[0])
				obj.printAllKeys("Inc " + tt.args[0])
			case "dec":
				obj.Dec(tt.args[0])
				obj.printAllKeys("Dec " + tt.args[0])
			case "getMaxKey":
				obj.printAllKeys("GetMaxKey")
				got := obj.GetMaxKey()
				if got != tt.want {
					t.Fatalf("expected %v, got %v", tt.want, got)
				}
			case "getMinKey":
				obj.printAllKeys("GetMinKey")
				got := obj.GetMinKey()
				if got != tt.want {
					t.Fatalf("expected %v, got %v", tt.want, got)
				}
			}
		}
	})
}
