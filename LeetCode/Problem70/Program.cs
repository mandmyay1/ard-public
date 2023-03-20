/* 
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/
public class Solution {
    Dictionary<int, int> cache = new Dictionary<int, int>();
    public int ClimbStairs(int n) {
        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }

        int nMinus1;
        if (cache.ContainsKey(n - 1)) {
            nMinus1 = cache[n - 1];
        } else {
            nMinus1 = ClimbStairs(n - 1);
            cache.Add(n - 1, nMinus1);
        }

        int nMinus2;
        if (cache.ContainsKey(n - 2)) {
            nMinus2 = cache[n - 2];
        } else {
            nMinus2 = ClimbStairs(n - 2);
            cache.Add(n - 2, nMinus2);
        }

        return nMinus1 + nMinus2;
    }
}