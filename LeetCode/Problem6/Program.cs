/*
https://leetcode.com/problems/zigzag-conversion/description/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
*/
public class Solution {
    public string Convert(string s, int numRows) {
        List<List<char>> arr = new List<List<char>>(numRows);
        for (int i = 0; i < numRows; i++) {
            arr.Add(new List<char>());
        }
        bool goingDown = true;
        int pos = 0;
        int currentList = 0;

        while (pos < s.Length){
            char c = s[pos];
            if (goingDown){
                List<char> listToAppendTo = arr[currentList];
                listToAppendTo.Add(c);

                if (numRows > 1) {
                    // Switch from down to up
                    if (currentList + 1 >= numRows) {
                        goingDown = false;
                        currentList--;
                    }
                    else {
                        currentList++;
                    }
                }
            }
            else {
                arr[currentList].Add(c);
                for (int i = 0; i < numRows; i++) {
                    if (i != currentList) {
                        arr[i].Add(' ');
                    }
                }
                
                if (numRows > 1) {
                    // Switch from up to down
                    if (currentList - 1 < 0) {
                        goingDown = true;
                        currentList++;
                    }
                    else {
                        currentList--;
                    }
                }
            }
            pos++;
        }

        List<char> retList = new List<char>(s.Length);
        foreach (List<char> row in arr) {
            Console.WriteLine(string.Join("", row));
            foreach (char c in row) {
                if (c != ' '){
                    retList.Add(c);
                }
            }
        }
        string ret = string.Join("", retList);
        return ret;
    }
    static void Main(string[] args){
        //Console.WriteLine(new Solution().Convert("PAYPALISHIRING", 4));
        //Console.WriteLine(new Solution().Convert("PAYPALISHIRING", 3));
        Console.WriteLine(new Solution().Convert("AB", 1));
    }
}