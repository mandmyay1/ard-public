/**
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 * 
 * You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
 */
public class Problem21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) { return list2; }
        if (list2 == null) { return list1; }

        ListNode head = null;
        ListNode current = null;

        if (list1.val < list2.val) {
            head = list1;
            current = list1;
            list1 = list1.next;
        } else {
            head = list2;
            current = list2;
            list2 = list2.next;
        }

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                current.next = list1;
                current = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                current = list2;
                list2 = list2.next;
            }
        }

        while (list1 != null) {
            current.next = list1;
            current = list1;
            list1 = list1.next;
        }
        while (list2 != null) {
            current.next = list2;
            current = list2;
            list2 = list2.next;
        }

        return head;
    }
    /*class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }*/
    
}
