// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
/**
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
*/
public class Solution {
    public IList<string> LetterCombinations(string digits) {
        IList<string> returnList = new List<string>();
        foreach (char c in digits) {
            List<string> toAppend = GenerateListForCharacter(c);

            if (returnList.Count == 0) {
                returnList = toAppend;
            }
            else {
                IList<string> newList = new List<string>();
                foreach (string existing in returnList) {
                    foreach (string append in toAppend) {
                        newList.Add(existing + append);
                    }
                }
                returnList = newList;
            }
        }
        return returnList;
    }
    private List<string> GenerateListForCharacter(char c) {
        if (c == '2') {
            return new List<string> {"a", "b", "c"};
        }
        if (c == '3') {
            return new List<string> {"d", "e", "f"};
        }
        if (c == '4') {
            return new List<string> {"g", "h", "i"};
        }
        if (c == '5') {
            return new List<string> {"j", "k", "l"};
        }
        if (c == '6') {
            return new List<string> {"m", "n", "o"};
        }
        if (c == '7') {
            return new List<string> {"p", "q", "r", "s"};
        }
        if (c == '8') {
            return new List<string> {"t", "u", "v"};
        }
        if (c == '9') {
            return new List<string> {"w", "x", "y", "z"};
        }
        return null;
    }
    static void Main(string[] args){
        foreach (string res in new Solution().LetterCombinations("23")) {
            Console.WriteLine(res);
        }
        foreach (string res in new Solution().LetterCombinations("")) {
            Console.WriteLine(res);
        }
        foreach (string res in new Solution().LetterCombinations("2")) {
            Console.WriteLine(res);
        }
    }
}
