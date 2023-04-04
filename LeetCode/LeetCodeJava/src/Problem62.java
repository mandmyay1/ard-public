/**
 * https://leetcode.com/problems/unique-paths/description/
 * 
 * There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
 * The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
 * Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
 */

public class Problem62 {
    int[][] cache;
    public int uniquePaths(int m, int n) {
        cache = new int[m][n];
        cache[0][0] = 1;

        return uniquePathsRecurse(m-1, n-1);
    }
    public int uniquePathsRecurse(int m, int n) {
        if (m < 0) { return 0; }
        if (n < 0) { return 0; }
        //if (m == 0 && n == 0) { return 1; }
        if (cache[m][n] != 0) { return cache[m][n]; }

        int values = uniquePathsRecurse(m - 1, n) + uniquePathsRecurse(m, n - 1);
        cache[m][n] = values;
        return values;
    }
    public static void main(String[] args) {
        System.out.println(new Problem62().uniquePaths(3, 2));
        System.out.println(new Problem62().uniquePaths(3, 7));
    }
}
