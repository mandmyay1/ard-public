/**
 * https://leetcode.com/problems/set-matrix-zeroes/description/
 * 
 * Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
 */

public class Problem73 {
    public void setZeroes(int[][] matrix) {
        int xLength = matrix.length;
        int yLength = matrix[0].length;
        boolean[] hasZeroX = new boolean[xLength];
        boolean[] hasZeroY = new boolean[yLength];

        for (int i = 0; i < xLength; i++) {
            for (int j = 0; j < yLength; j++) {
                if (matrix[i][j] == 0) {
                    hasZeroX[i] = true;
                    hasZeroY[j] = true;
                }
            }
        }

        for (int i = 0; i < xLength; i++) {
            if (hasZeroX[i]) {
                // Blank out all values in this row
                for (int k = 0; k < yLength; k++) {
                    matrix[i][k] = 0;
                }
            }
        }
        for (int j = 0; j < yLength; j++) {
            if (hasZeroY[j]) {
                // Blank out all values in this column
                for (int k = 0; k < xLength; k++) {
                    matrix[k][j] = 0;
                }
            }
        }
    }
}
