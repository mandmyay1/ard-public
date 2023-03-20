/*
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
*/
public class Solution {
    Dictionary<int, int> cache = new Dictionary<int, int>();
    public int CoinChange(int[] coins, int amount) {
        cache.Add(0, 0);
        foreach (int coin in coins) {
            if (!cache.ContainsKey(coin)) {
                cache.Add(coin, 1);
            }
        }

        for (int cent = 1; cent <= amount; cent++) {
            if (cache.ContainsKey(cent)) { continue; }

            int minValue = int.MaxValue;
            foreach (int coin in coins) {
                if (cache.ContainsKey(cent - coin)) {
                    int newValue = cache[cent - coin] + 1;
                    minValue = Math.Min(newValue, minValue);
                    cache[cent] = minValue;
                }
            }
        }
        if (cache.ContainsKey(amount)) {
            return cache[amount];
        }
        return -1;
    }

    static void Main(string[] args){
        Console.WriteLine(new Solution().CoinChange(new[] {1, 2, 5}, 11));
        Console.WriteLine(new Solution().CoinChange(new[] {2}, 3));
        Console.WriteLine(new Solution().CoinChange(new[] {1}, 0));
        Console.WriteLine(new Solution().CoinChange(new[] {281,20,251,251}, 7323));
    }
}