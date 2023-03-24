/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * 
 * You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
 */

public class Problem23 {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = null;
        ListNode current = null;

        // Find head
        int minPos = findMinPosition(lists);
        if (minPos == -1) { return null; }

        head = lists[minPos];
        current = head;
        lists[minPos] = lists[minPos].next;

        minPos = findMinPosition(lists);
        while (minPos != -1) {
            current.next = lists[minPos];
            current = lists[minPos];
            lists[minPos] = lists[minPos].next;
            minPos = findMinPosition(lists);
        }

        return head;
    }

    private int findMinPosition(ListNode[] lists) {
        int minVal = Integer.MAX_VALUE;
        int minPos = Integer.MAX_VALUE;
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null && lists[i].val < minVal) {
                minVal = lists[i].val;
                minPos = i;
            }
        }
        // All lists are empty
        if (minPos == Integer.MAX_VALUE) { return -1; }

        return minPos;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(4);
        list1.next.next = new ListNode(5);

        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        ListNode list3 = new ListNode(2);
        list3.next = new ListNode(6);

        ListNode[] arr = new ListNode[3];
        arr[0] = list1;
        arr[1] = list2;
        arr[2] = list3;

        new Problem23().mergeKLists(arr);
    }

}

