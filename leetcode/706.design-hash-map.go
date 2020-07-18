package leetcode

const BucketSize = 8192

type listNode struct {
	key   int
	value int
	next  *listNode
}

type MyHashMap struct {
	data [BucketSize]*listNode
}

func Constructor() MyHashMap {
	return MyHashMap{}
}

func (this *MyHashMap) Put(key int, value int) {
	bucket := key % BucketSize
	node := this.data[bucket]
	if node == nil {
		node = &listNode{
			key:   key,
			value: value,
			next:  nil,
		}
		this.data[bucket] = node
		return
	}
	if node.key == key {
		node.value = value
		return
	}

	for ; node.next != nil && node.next.key != key; node = node.next {
	}
	if node.next == nil {
		node.next = &listNode{
			key:   key,
			value: value,
			next:  nil,
		}
	} else {
		node.next.value = value
	}
}

func (this *MyHashMap) Get(key int) int {
	bucket := key % BucketSize
	for node := this.data[bucket]; node != nil; node = node.next {
		if node.key == key {
			return node.value
		}
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	bucket := key % BucketSize
	node := this.data[bucket]
	if node == nil {
		return
	}
	if node.key == key {
		this.data[bucket] = node.next
		return
	}

	for ; node.next != nil; node = node.next {
		if node.next.key == key {
			node.next = node.next.next
			break
		}
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
