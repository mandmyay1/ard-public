/**
 * https://leetcode.com/problems/number-of-1-bits/description/
 * 
 * Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 */

public class Problem191 {
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
    public static void main(String[] args) {
        System.out.println(new Problem191().hammingWeight(00000000000000000000000000001011));
        System.out.println(new Problem191().hammingWeight(00000000000000000000000010000000));
        //System.out.println(new Problem191().hammingWeight(01111111111111111111111111111101));
    }
}
