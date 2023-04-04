/*
 * https://leetcode.com/problems/pacific-atlantic-water-flow/description/
 * 
 * There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
 * 
 */

import java.util.ArrayList;
import java.util.List;

public class Problem417 {

    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int height = heights.length;
        int width = heights[0].length;
        boolean[][] flowsToAtlantic = new boolean[height][width];
        boolean[][] flowsToPacific = new boolean[height][width];

        List<List<Integer>> atlanticQueue = new ArrayList<List<Integer>>();
        List<List<Integer>> pacificQueue = new ArrayList<List<Integer>>();


        for (int row = 0; row < height; row++) {
            flowsToAtlantic[row][width -1] = true;
            atlanticQueue.add(createList(row, width -1));
            flowsToPacific[row][0] = true;
            pacificQueue.add(createList(row, 0));
        }
        for (int col = 0; col < width; col++) {
            flowsToAtlantic[height -1][col] = true;
            atlanticQueue.add(createList(height -1, col));
            flowsToPacific[0][col] = true;
            pacificQueue.add(createList(0, col));
        }

        flowsToAtlantic = bfs(heights, flowsToAtlantic, atlanticQueue);
        flowsToPacific = bfs(heights, flowsToPacific, pacificQueue);

        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                if (flowsToAtlantic[row][col] && flowsToPacific[row][col]) {
                    result.add(createList(row, col));
                }
            }
        }


        return result;
    }

    private boolean[][] bfs(int[][] heights, boolean[][] visited, List<List<Integer>> queue) {
        int height = heights.length;
        int width = heights[0].length;

        while (!queue.isEmpty()) {
            List<Integer> validLocation = queue.get(0);
            queue.remove(0);
            int row = validLocation.get(0);
            int col = validLocation.get(1);
            int heightAtValidLocation = heights[row][col];

            int right = col + 1;
            int left = col - 1;
            int up = row - 1;
            int down = row + 1;

            if (right < width && visited[row][right] == false) {
                if (heights[row][right] >= heightAtValidLocation) {
                    visited[row][right] = true;
                    queue.add(createList(row, right));
                }
            }
            if (left >= 0 && visited[row][left] == false) {
                if (heights[row][left] >= heightAtValidLocation) {
                    visited[row][left] = true;
                    queue.add(createList(row, left));
                }
            }
            if (up >= 0 && visited[up][col] == false) {
                if (heights[up][col] >= heightAtValidLocation) {
                    visited[up][col] = true;
                    queue.add(createList(up, col));
                }
            }
            if (down < height && visited[down][col] == false) {
                if (heights[down][col] >= heightAtValidLocation) {
                    visited[down][col] = true;
                    queue.add(createList(down, col));
                }
            }
        }
        return visited;
    }

    private ArrayList<Integer> createList(int row, int col) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        result.add(row);
        result.add(col);
        return result;
    }

    public static void main(String[] args) {
        List<List<Integer>> result;

        // [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        int[][] heights = new int[5][5];
        heights[0][0] = 1;
        heights[0][1] = 2;
        heights[0][2] = 2;
        heights[0][3] = 3;
        heights[0][4] = 5;

        heights[1][0] = 3;
        heights[1][1] = 2;
        heights[1][2] = 3;
        heights[1][3] = 4;
        heights[1][4] = 4;

        heights[2][0] = 2;
        heights[2][1] = 4;
        heights[2][2] = 5;
        heights[2][3] = 3;
        heights[2][4] = 1;

        heights[3][0] = 6;
        heights[3][1] = 7;
        heights[3][2] = 1;
        heights[3][3] = 4;
        heights[3][4] = 5;

        heights[4][0] = 5;
        heights[4][1] = 1;
        heights[4][2] = 1;
        heights[4][3] = 2;
        heights[4][4] = 4;
        result = new Problem417().pacificAtlantic(heights);
        System.out.print("[");
        for (List<Integer> x : result) {
            System.out.print("[");
            for (Integer y : x) {
                System.out.print(y + " ");

            }
            System.out.print("]");
        }
        System.out.println("]");

        // [[1,1],[1,1],[1,1]]
        int[][] heights2 = new int[3][2];
        heights2[0][0] = 1;
        heights2[0][1] = 1;
        heights2[1][0] = 1;
        heights2[1][1] = 1;
        heights2[2][0] = 1;
        heights2[2][1] = 1;

        
        result = new Problem417().pacificAtlantic(heights2);
        System.out.print("[");
        for (List<Integer> x : result) {
            System.out.print("[");
            for (Integer y : x) {
                System.out.print(y + " ");

            }
            System.out.print("]");
        }
        System.out.println("]");
        
        //[[2,1],[1,2]]
        int[][] heights3 = new int[2][2];
        heights3[0][0] = 1;
        heights3[0][1] = 1;
        heights3[1][0] = 1;
        heights3[1][1] = 2;
        result = new Problem417().pacificAtlantic(heights3);
        System.out.print("[");
        for (List<Integer> x : result) {
            System.out.print("[");
            for (Integer y : x) {
                System.out.print(y + " ");

            }
            System.out.print("]");
        }
        System.out.println("]");
    }

}
