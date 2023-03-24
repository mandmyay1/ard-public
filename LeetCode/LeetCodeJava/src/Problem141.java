import java.util.HashSet;

/**
 * https://leetcode.com/problems/linked-list-cycle/description/
 * 
 * Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
 */
public class Problem141 {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> cache = new HashSet<ListNode>();
        while (head != null) {
            if (cache.contains(head)) {
                return true;
            }
            cache.add(head);
            head = head.next;
        }
        return false;
    }
}

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}