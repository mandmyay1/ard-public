/*
 * https://leetcode.com/problems/reverse-linked-list/description/
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 */

public class Problem206 {
    public ListNode reverseList(ListNode head) {
        if (head == null) { return null; }

        ListNode prev = null;
        ListNode current = head;
        ListNode next = head.next; 

        while (current.next != null) {
            current.next = prev;
            prev = current;
            current = next;
            next = next.next;
        }
        current.next = prev;
        
        return current;
    }
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
