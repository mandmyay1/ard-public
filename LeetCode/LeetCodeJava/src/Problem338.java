/**
 * https://leetcode.com/problems/counting-bits/description/
 * 
 * Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
 */
public class Problem338 {
    public int[] countBits(int n) {
        int[] arr = new int[n + 1];
        for (int i = 0; i <= n; i++)  {
            arr[i] = hammingWeight(i);
        }
        return arr;
    }
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;

        for (int i = 0; i < 32; i++) {
            int even = n & 1;
            if (even == 1) { count++; }
            n = n >> 1;
        }
        return count;
    }
    public static void printArr(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            if (i != 0) {
                System.out.print(",");
            }
            System.out.print(arr[i]);
        }
        System.out.println("]");
    }
    public static void main(String[] args) {
        printArr(new Problem338().countBits(2));
        printArr(new Problem338().countBits(5));
        printArr(new Problem338().countBits(9));
        printArr(new Problem338().countBits(27));
    }
}
