import java.util.HashMap;

/*https://leetcode.com/problems/jump-game/description/
 * 
 * You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 */
public class Problem55 {
    HashMap<Integer, Boolean> cache = new HashMap<Integer, Boolean>();
    public boolean canJump(int[] nums) {
        boolean[] cache2 = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            cache2[i] = false;
        }

        cache2[nums.length - 1] = true;
        for (int j = nums.length -2; j >= 0; j--) {
            int valAt = nums[j];
            for (int k = 1; k <= valAt; k++) {
                if (j + k >= nums.length) { continue; }
                if (cache2[j + k]) {
                    cache2[j] = true;
                }
            }
        }

        return cache2[0];
    }
    public static void main(String[] args) throws Exception {
        System.out.println(new Problem55().canJump(new int[] {2,3,1,1,4}));
        System.out.println(new Problem55().canJump(new int[] {3,2,1,0,4}));
    }
}