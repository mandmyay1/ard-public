import java.util.ArrayList;

/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 * 
 * Given the head of a linked list, remove the nth node from the end of the list and return its head.
 */
public class Problem19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ArrayList<ListNode> cache = new ArrayList<ListNode>();
        ListNode current = head;
        while (current != null) {
            cache.add(current);
            current = current.next;
        }
        int posToRemove = cache.size() - n;
        int posPrev = cache.size() - n - 1;

        ListNode itemToRemove = cache.get(posToRemove);

        if (posPrev < 0) {
            // first position to remove, just return second element
            return itemToRemove.next;
        }
        ListNode prevItem = cache.get(posPrev);
        prevItem.next = itemToRemove.next;

        return head;
    }
}
