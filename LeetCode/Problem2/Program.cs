// https://leetcode.com/problems/add-two-numbers/description/
/**
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
**/
  public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode next = null;
        bool carry = false;
        while (l1 != null || l2 != null) {
            int v1 = 0;
            if (l1 != null) { 
                v1 = l1.val;
                l1 = l1.next;
            }
            int v2 = 0;
            if (l2 != null) { 
                v2 = l2.val; 
                l2 = l2.next;
            }

            int sum = v1 + v2;
            if (carry) {
                sum++;
            }

            if (sum >= 10) {
                sum = sum%10;
                carry = true;
            }
            else {
                carry = false;
            }
            ListNode newNd = new ListNode(sum);
            if (null == head) {
                head = newNd;
            } else {
                next.next = newNd;
            }
            next = newNd;
        }
        if (carry) {
            ListNode newNd = new ListNode(1);
            next.next = newNd;
        }


        return head;
    }
}