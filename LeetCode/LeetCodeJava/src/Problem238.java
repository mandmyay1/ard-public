/**
 * https://leetcode.com/problems/product-of-array-except-self/
 * 
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
 */
public class Problem238 {
    public int[] productExceptSelfN2(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = 1;
            for (int j = 0; j < nums.length; j++) {
                if (i != j) {
                    res[i] = res[i] * nums[j];
                }
            }
        }
        return res;
    }

    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];

        pre[0] = 1;
        post[nums.length - 1] = 1;

        for (int i = 1; i < nums.length; i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for (int i = nums.length - 2; i >= 0; i--) {
            post[i] = post[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            pre[i] = pre[i] * post[i];
        }
        return pre;
    }

    public static void printArr(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) {
                System.out.print(",");
            }
            System.out.print(arr[i]);
        }
        System.out.println("]");
    }
    public static void main(String[] args) {
        int[] arr = new int[] {1, 2, 3, 4};
        printArr(new Problem238().productExceptSelf(arr));
    }
}
