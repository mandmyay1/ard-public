/**
 * https://leetcode.com/problems/maximum-subarray/
 * 
 * Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 Approach: sliding window. If the current window is less than the next item, then the window is over and needs to be reset to the next item
 */

class Problem53 {
    public int maxSubArray(int[] nums) {
        int left = 0;
        int right = 0;

        long currentSum = 0;
        long maxValue = Long.MIN_VALUE;

        while (right < nums.length && left <= right) {
            // Maintain a list of the running sum from `left` position
            currentSum = currentSum + nums[right];
            // If the current sum is smaller than the next item, the current window is over and needs to be reset to that next item.
            if (currentSum < nums[right]) {
                left++;
                right = left;
                currentSum = nums[left];
            }
            right++;
            maxValue = Math.max(currentSum, maxValue);
        }
        return (int)maxValue;
    }
}