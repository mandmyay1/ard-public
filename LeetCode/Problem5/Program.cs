/*
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest 
palindromic
 
substring
 in s.
 */

public class Solution {
    public string LongestPalindrome(string s) {
        int longestPalindrome = 0;
        string longestPalindromeStr = string.Empty;
        int start = 0;

        while (start + longestPalindrome < s.Length){
            int end = start + longestPalindrome;
            while (end < s.Length){
                if (IsPalindrome(s, start, end)) {
                    longestPalindrome = end - start + 1;
                    longestPalindromeStr = s.Substring(start, longestPalindrome);
                }
                end++;
            }
            start++;
        }
        return longestPalindromeStr;
    }

    private bool IsPalindrome(string input, int posx, int posy){
        while (posx < posy){
            if (input[posx] != input[posy]) { return false; }

            posx++;
            posy--;
        }
        return true;
    }

    static void Main(string[] args){
        Console.WriteLine(new Solution().LongestPalindrome("babad"));
        Console.WriteLine(new Solution().LongestPalindrome("cbbd"));
    }
}
