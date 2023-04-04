public class Problem48 {
    public void rotate(int[][] matrix) {
        int xLength = matrix.length;
        int extra = 0;
        if (xLength % 2 != 0) {
            extra = 1;
        }

        for (int i  = 0; i < xLength / 2; i++) {
            for (int j = 0; j < xLength / 2 + extra; j++) {
                int pos1 = matrix[i][j];
                int pos2 = matrix[j][xLength - i - 1];
                int pos3 = matrix[xLength - j - 1][i];
                int pos4 = matrix[xLength - i - 1][xLength - j - 1];

                matrix[i][j] = pos3;
                matrix[j][xLength - i - 1] = pos1;
                matrix[xLength - j - 1][i] = pos4;
                matrix[xLength - i - 1][xLength - j - 1] = pos2;
            }
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(" ");
                System.out.print(matrix[i][j]);
            }
            System.out.println("]");
        }
    }
    public static void main(String[] args) {

        int[][] input = new int[3][3];
        input[0][0] = 1;
        input[0][1] = 2;
        input[0][2] = 3;
        input[1][0] = 4;
        input[1][1] = 5;
        input[1][2] = 6;
        input[2][0] = 7;
        input[2][1] = 8;
        input[2][2] = 9;

        new Problem48().rotate(input);
        printMatrix(input);

        int[][] input2 = new int[4][4];
        input2[0][0] = 5;
        input2[0][1] = 1;
        input2[0][2] = 9;
        input2[0][3] = 11;
        input2[1][0] = 2;
        input2[1][1] = 4;
        input2[1][2] = 8;
        input2[1][3] = 10;
        input2[2][0] = 13;
        input2[2][1] = 3;
        input2[2][2] = 6;
        input2[2][3] = 7;
        input2[3][0] = 15;
        input2[3][1] = 14;
        input2[3][2] = 12;
        input2[3][3] = 16;
        new Problem48().rotate(input2);
        printMatrix(input2);

        int[][] input3 = new int[2][2];
        input3[0][0] = 1;
        input3[0][1] = 2;
        input3[1][0] = 3;
        input3[1][1] = 4;
        new Problem48().rotate(input3);
        printMatrix(input3);
    }
}
