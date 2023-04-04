/*
 * https://leetcode.com/problems/number-of-islands/description/
 * 
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 */

import java.util.ArrayList;
import java.util.List;

public class Problem200 {
    public int numIslands(char[][] grid) {
        int height = grid.length;
        int width = grid[0].length;

        int[][] islandGrid = new int[height][width];
        int islandNum = 0;

        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                int islandNumAtPosition = islandGrid[row][col];
                if (islandNumAtPosition != 0) { continue; };

                char charAtPosition = grid[row][col];
                if (charAtPosition == '1') {
                    islandNum++;
                    List<List<Integer>> queue = new ArrayList<List<Integer>>();
                    queue.add(createList(row, col));
                    islandGrid[row][col] = islandNum;
                    bfs(grid, islandGrid, islandNum, queue);
                }
            }
        }
        return islandNum;
    }
    private void bfs(char[][] grid, int[][] islandGrid, int islandNum, List<List<Integer>> queue) {
        int height = grid.length;
        int width = grid[0].length;

        while (!queue.isEmpty()) {
            List<Integer> top = queue.get(0);
            queue.remove(0);
            int row = top.get(0);
            int col = top.get(1);

            islandGrid[row][col] = islandNum;

            int right = col + 1;
            int left = col - 1;
            int up = row - 1;
            int down = row + 1;

            if (right < width && islandGrid[row][right] == 0 && grid[row][right] == '1') {
                islandGrid[row][right] = islandNum;
                queue.add(createList(row, right));
            }
            if (left >= 0 && islandGrid[row][left] == 0 && grid[row][left] == '1') {
                islandGrid[row][left] = islandNum;
                queue.add(createList(row, left));
            }
            if (up >= 0 && islandGrid[up][col] == 0 && grid[up][col] == '1') {
                islandGrid[up][col] = islandNum;
                queue.add(createList(up, col));
            }
            if (down< height && islandGrid[down][col] == 0 && grid[down][col] == '1') {
                islandGrid[down][col] = islandNum;
                queue.add(createList(down, col));
            }
        }
    }

    private List<Integer> createList(int row, int col) {
        List<Integer> starting = new ArrayList<Integer>();
        starting.add(row);
        starting.add(col);
        return starting;
    }
}
