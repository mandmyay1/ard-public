/**
 * https://leetcode.com/problems/longest-increasing-subsequence/description/
 * 
 * Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
 */

public class Problem300 {
    public int lengthOfLIS(int[] nums) {
        int lis[] = new int[nums.length];
        lis[nums.length -1] = 1;
        int overallMax = 1;

        for (int i = nums.length -2; i >= 0; i--) {
            int valAtI = nums[i];
            int maxFound = 1;
            for (int j = i +1; j < nums.length; j++) {
                int valAtJ = nums[j];
                if (valAtJ > valAtI) {
                    maxFound = Math.max(maxFound, 1 + lis[j]);
                }
            }
            lis[i] = maxFound;
            overallMax = Math.max(overallMax, maxFound);
        }
        return overallMax;
    }
}
