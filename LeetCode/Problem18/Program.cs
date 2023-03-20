// https://leetcode.com/problems/4sum/description/
/*
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
*/

public class Solution {
    public IList<IList<int>> FourSum(int[] nums, int target) {
        Array.Sort(nums);
        HashSet<(int, int, int, int)> hashSet = new HashSet<(int, int, int, int)>();

        for (int i = 0; i < nums.Length; i++) {

            for (int j = i + 1; j < nums.Length; j++) {
                int k = j + 1;
                int h = nums.Length - 1;

                while (k < h) {
                    long sum = (long)nums[i] + (long)nums[j] + (long)nums[k] + (long)nums[h];
                    if (sum == target) {
                        hashSet.Add((nums[i], nums[j], nums[k], nums[h]));
                        Console.WriteLine("added " + nums[i] + "" +  nums[j] +"" +  nums[k] + "" + nums[h]);
                        k++;
                        h--;
                    }
                    else if (sum < target) {
                        k++;
                    }
                    else {
                        h--;
                    }
                }
            }
        }
        IList<IList<int>> returnList = new List<IList<int>>();
        foreach ((int v1, int v2, int v3, int v4) in hashSet) {
            returnList.Add(new List<int> {v1, v2, v3, v4});
        }
        Console.WriteLine("Number items in list = " + returnList.Count);
        return returnList;
    }
    static void Main(string[] args){
        Console.WriteLine(new Solution().FourSum(new[] {1,0,-1,0,-2,2}, 0));
        Console.WriteLine(new Solution().FourSum(new[] {2,2,2,2,2}, 8));
        Console.WriteLine(new Solution().FourSum(new[] {1000000000,1000000000,1000000000,1000000000}, -294967296));
    }
}