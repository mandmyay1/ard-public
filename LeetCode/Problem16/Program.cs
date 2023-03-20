/**
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
*/

public class Solution { 
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int closestSum = Int32.MaxValue;
        for (int left = 0; left < nums.Length - 2; left++) {
            int s1 = nums[left];
            for (int right = left + 2; right < nums.Length; right++){
                int s3 = nums[right];
                for (int mid = left + 1; mid < right; mid++) {
                    int s2 = nums[mid];
                    int sum = s1 + s2 + s3;
                    if (Math.Abs(sum - target) < Math.Abs(closestSum - target)) {
                        Console.WriteLine("" + s1 + ", " + s2 + ", " + s3 + "=" + sum + ". Math.Abs(sum - target)=" + Math.Abs(sum - target) + " Math.Abs(closestSum - target)=" + Math.Abs(closestSum - target));
                        closestSum = sum;
                    }
                }
            }
        }
        return closestSum;
    }    
    static void Main(string[] args){
        Console.WriteLine(new Solution().ThreeSumClosest(new[] {7,9,11,13,17,21,42,68}, 88));
        Console.WriteLine(new Solution().ThreeSumClosest(new[] {-1,2,1,-4}, 88));
        Console.WriteLine(new Solution().ThreeSumClosest(new[] {0,0,0}, 1));
        Console.WriteLine(new Solution().ThreeSumClosest(new[] {4,0,5,-5,3,3,0,-4,-5}, -2));
    }
}
