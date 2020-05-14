class AddTwoNumber {
    // leetcode 2
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int ex = 0;
        ListNode dummy = new ListNode(0), curr = dummy;
        while (l1 != null || l2 != null) {
            int val = ex;
            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }
            ex = val / 10;

            ListNode node = new ListNode(val % 10);
            curr.next = node;
            curr = node;
        }
        if (ex > 0) curr.next = new ListNode(ex);
        return dummy.next;
    }
}