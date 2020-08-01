package sieunhan.algorithm.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class LFUCache {

    static class ListNode {
        int key;
        int value;
        long last;
        int freq;
        ListNode prev;
        ListNode next;

        ListNode(int key, int val) {
            this.key = key;
            this.value = val;
            this.last = System.currentTimeMillis();
            this.freq = 1;
        }
    }

    private int capacity;
    private ListNode head = new ListNode(0, 0);
    private Map<Integer, ListNode> data = new HashMap<>();

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.head.freq = 0;
    }

    private void insertNode(ListNode curr, ListNode node) {
        node.next = curr.next;
        node.prev = curr;

        if (curr.next != null) {
            curr.next.prev = node;
        }
        curr.next = node;
    }

    private void removeNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveRecentNode(ListNode node) {
        ListNode curr = node;
        while (curr.next != null && curr.next.freq < node.freq) {
            curr = curr.next;
        }
        if (curr == node) return;

        // Remove recent accessed node
        this.removeNode(node);

        // Insert recent node new position
        this.insertNode(curr, node);
    }

    private void printList() {
        ListNode node = head.next;
        while (node != null) {
            System.out.print("(" + node.key + ":" + node.value + ")");
            System.out.print("->");
            node = node.next;
        }
    }

    public int get(int key) {
        ListNode node = data.get(key);
        if (node == null) return -1;

        node.freq += 1;
        node.last = System.currentTimeMillis();

        this.moveRecentNode(node);

        return node.value;
    }

    public void put(int key, int value) {
        ListNode node = data.get(key);
        if (node == null) {
            node = new ListNode(key, value);
            // Insert new node to the begin of list
            if (head.next != null) {
                this.insertNode(head, node);
            } else {
                this.head.next = node;
            }
            data.put(key, node);
        } else {
            node.freq += 1;
            node.last = System.currentTimeMillis();
            this.moveRecentNode(node);

            if (data.size() == capacity) {
                ListNode lfNode = head.next;

                // Remove tail node
                head.next = lfNode.next;

                // Remove LF node data
                data.remove(lfNode.key);
            }
        }
    }

    public static void main(String[] args) {
        LFUCache cache = new LFUCache(100);
        Random r = new Random();
        for (int i = 0; i < 20; i++) {
            int key = r.nextInt(5);
            cache.put(key, r.nextInt(10));
            cache.printList();
            System.out.println(" " + key);
        }
    }
}
