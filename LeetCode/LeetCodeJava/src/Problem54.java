import java.util.ArrayList;
import java.util.List;

public class Problem54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> returnList = new ArrayList<Integer>();

        int yLength = matrix.length;
        int xLength = matrix[0].length;

        int numberRotations = 0;

        int x = 0;
        int y = 0;

        int xInc = 1;
        int yInc = 0;

        // 1 = right
        // 2 = down
        // 3 = left
        // 4 = up
        int direction = 1;


        for (int counter = 0; counter < xLength * yLength; counter++) {
            int val = matrix[y][x];
            returnList.add(val);
            if (direction == 1 && x + xInc >= xLength - numberRotations) {
                xInc = 0;
                yInc = 1;
                direction = 2;
            }
            else if (direction == 2 && y + yInc >= yLength - numberRotations) {
                xInc = -1;
                yInc = 0;
                direction = 3;
            }
            else if (direction == 3 && x + xInc < numberRotations) {
                xInc = 0;
                yInc = -1;
                numberRotations += 1;
                direction = 4;
            }
            else if (direction == 4 && y + yInc < numberRotations) {
                xInc = 1;
                yInc = 0;
                direction = 1;
            }

            x = x + xInc;
            y = y + yInc;
        }
        return returnList;
    }

    public static void main(String[] args) {
        int[][] input = new int[4][4];
        input[0][0] = 1;
        input[0][1] = 2;
        input[0][2] = 3;
        input[0][3] = 4;
        input[1][0] = 5;
        input[1][1] = 6;
        input[1][2] = 7;
        input[1][3] = 8;
        input[2][0] = 9;
        input[2][1] = 10;
        input[2][2] = 11;
        input[2][3] = 12;
        input[3][0] = 13;
        input[3][1] = 14;
        input[3][2] = 15;
        input[3][3] = 16;
        List<Integer> val = new Problem54().spiralOrder(input);
        System.out.print("[");
        for (int i = 0; i < val.size(); i++) {
            System.out.print(val.get(i));
            System.out.print(" ");
        }
        System.out.println("]");
    }
}
