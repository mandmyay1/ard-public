// https://leetcode.com/problems/longest-substring-without-repeating-characters/
/*
Given a string s, find the length of the longest 
substring
 without repeating characters.
 */
 
 public class Solution {
    public int LengthOfLongestSubstring(string s) {
        Dictionary<char, int> map = new Dictionary<char, int>();
        int left = 0;
        int right = 0;
        int length = s.Length;
        int maxLength = 0;

        while (right < length && left < length){
            char c = s[right];
            if (map.ContainsKey(c)){
                left = Math.Max(map[c] + 1, left);
            }
            map[c] = right;
            maxLength = Math.Max(maxLength, right - left + 1);
            right++;
        }
        return maxLength;
    }
}
