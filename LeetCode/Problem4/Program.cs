// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
/* Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
*/
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int combinedLength = nums1.Length + nums2.Length;
        int[] combinedArray = new int[combinedLength];
        
        int p1 = 0, p2 = 0;
        for (int i = 0; i < combinedLength; i++) {
            
            if (p1 >= nums1.Length){
                combinedArray[i] = nums2[p2];
                p2++;
                continue;
            }
            if (p2 >= nums2.Length){
                combinedArray[i] = nums1[p1];
                p1++;
                continue;
            }
            
            int n1 = nums1[p1];
            int n2 = nums2[p2];
            
            if (n1 < n2){
                combinedArray[i] = n1;
                p1++;
            }
            else {
                combinedArray[i] = n2;
                p2++;
            }
        }
        
        if (combinedLength % 2 == 1){
            // odd
            return combinedArray[combinedLength/2];
        }
        else {
            // even
            return (float)(combinedArray[combinedLength/2-1] + combinedArray[combinedLength/2])/2;
        }
    }
}