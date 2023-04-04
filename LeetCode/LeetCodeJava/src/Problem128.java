/*
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 * 
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
 */

import java.util.HashSet;

public class Problem128 {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<Integer>(nums.length);
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int valAt = nums[i];
            hashSet.add(valAt);
            minVal = Math.min(minVal, valAt);
            maxVal = Math.max(maxVal, valAt);
        }
        
        int maxLength = 0;
        for (int i = 0; i < nums.length; i++) {
            int valAt = nums[i];
            if (hashSet.contains(valAt - 1)) {
                continue;
            }
            while (hashSet.contains(valAt)) {
                valAt++;
            }
            int currentLength = valAt - nums[i];
            maxLength = Math.max(currentLength, maxLength);
        }

        return maxLength;
    }
}
