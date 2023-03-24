import java.util.ArrayList;

/*
 * https://leetcode.com/problems/reorder-list/description/
 * 
 * You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
 */

public class Problem143 {
    public void reorderList(ListNode head) {
        if (head == null) { return; }

        ArrayList<ListNode> cache = new ArrayList<ListNode>();
        ListNode current = head;
        while (current != null) {
            cache.add(current);
            current = current.next;
        }

        current = head;
        ListNode next = current.next;
        int endNodePosition = cache.size() - 1;
        while (next != null && endNodePosition > 1) {
            ListNode endNode = cache.get(endNodePosition);
            if (endNode == next) { break; }
            ListNode endNodePrev = cache.get(endNodePosition - 1);

            current.next = endNode;
            endNodePrev.next = endNode.next;
            endNode.next = next;

            current = next;
            next = current.next;
            endNodePosition--;
        }
    }
}
