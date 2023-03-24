/**
 * https://leetcode.com/problems/reverse-bits/description/
 * Reverse bits of a given 32 bits unsigned integer.
 */

public class Problem190 {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        // int is 32 bits long
        for (int i = 0; i < 32; i++) {
            // find what is the trailing bit
            int bit = n & 1;
            // shift the existing bits over to make room for the current bit
            res = res << 1;
            // append the bit
            res = res | bit;
            // shift the input by 1
            n = n >> 1;
        }
        return res;
    }
    public static void main(String[] args) {
        System.out.println(new Problem190().reverseBits(00000000000000000000000000001011));
        //System.out.println(new Problem190().reverseBits(00000000000000000000000010000000));
        //System.out.println(new Problem191().hammingWeight(01111111111111111111111111111101));
    }
}
