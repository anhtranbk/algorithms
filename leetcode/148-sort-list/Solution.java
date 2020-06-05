package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class SortList {

    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    private ListNode mergeSortedList(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(-1);
        ListNode head = l3;
        while (l1 != null || l2 != null) {
            if (l1 != null && (l2 == null || l1.val < l2.val)) {
                l3.next = l1;
                l3 = l1;
                l1 = l1.next;
            } else {
                l3.next = l2;
                l3 = l2;
                l2 = l2.next;
            }
        }
        return head.next;
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode fast = head, slow = head, preSlow = slow;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            preSlow = slow;
            slow = slow.next;
        }
        preSlow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(slow);
        return mergeSortedList(left, right);
    }

    static void printList(ListNode node) {
        while (node != null) {
            System.out.print(node.val);
            if (node.next != null) System.out.print("->");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] input1 = new int[]{4, 2, 1, 3};
        int[] input2 = new int[]{-1, 5, 3, 4, 0};

        ListNode head1 = new ListNode(-1);
        ListNode curr = head1;
        for (int num : input1) {
            ListNode node = new ListNode(num);
            curr.next = node;
            curr = node;
        }
        head1 = head1.next;
        printList(head1);

        head1 = new SortList().sortList(head1);
        printList(head1);

        ListNode head2 = new ListNode(-1);
        curr = head2;
        for (int num : input2) {
            ListNode node = new ListNode(num);
            curr.next = node;
            curr = node;
        }
        head2 = head2.next;
        printList(head2);

        head2 = new SortList().sortList(head2);
        printList(head2);
    }
}
