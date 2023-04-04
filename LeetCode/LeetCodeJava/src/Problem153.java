/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 * 
 * Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
 */

public class Problem153 {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int middle = (right + left) / 2;

        while (middle != left && middle != right) {

            int valLeft = nums[left];
            int valRight = nums[right];
            int valMid = nums[middle];

            if (valRight <= valMid) {
                left = middle;
            }
            else if (valLeft >= valMid){
                right = middle;
            }
            else if (valLeft < valMid) {
                right = middle;
            }
            middle = (right + left) / 2;
        }

        return Math.min(nums[left], nums[right]);
    }
    public static void main(String[] args) {
        System.out.println(new Problem153().findMin(new int[] {4,5,6,7,0,1,2}));
        System.out.println(new Problem153().findMin(new int[] {0,1,2,4,5,6,7}));
        System.out.println(new Problem153().findMin(new int[] {3,4,5,1,2}));
        System.out.println(new Problem153().findMin(new int[] {11,13,15,17}));
    }
}
