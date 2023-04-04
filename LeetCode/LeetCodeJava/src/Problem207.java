// https://leetcode.com/problems/course-schedule/
/*
 * There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Problem207 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < prerequisites.length; i++) {
            int prereq = prerequisites[i][1];
            int postreq = prerequisites[i][0];

            List<Integer> prereqs;
            if (map.containsKey(postreq)) {
                prereqs = map.get(postreq);
            }
            else {
                prereqs = new ArrayList<Integer>();
                map.put(postreq, prereqs);
            }
            prereqs.add(prereq);
        }

        for (int courseNumber = 0; courseNumber < numCourses; courseNumber++) {
            if (map.containsKey(courseNumber)) {
                if (hasLoop(courseNumber, numCourses, map)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean hasLoop(int start, int numCourses, HashMap<Integer, List<Integer>> map) {
        boolean[] visited = new boolean[numCourses];
        visited[start] = true;

        List<Integer> queue = new ArrayList<Integer>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int courseNumber = queue.get(0);
            queue.remove(0);
            visited[courseNumber] = true;

            if (map.containsKey(courseNumber)) {
                List<Integer> prereqs = map.get(courseNumber);

                for (int i = 0; i < prereqs.size(); i++) {
                    int prereq = prereqs.get(i);
                    // Found a loop if the prereq is back to the beginning
                    if (prereq == start) {
                        return true;
                    }
                    // If we've already checked a course, don't need to check it again.
                    if (visited[prereq]) {
                        continue;
                    }
                    queue.add(prereq);
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] prerequisites = new int[2][2];
        prerequisites[0][0] = 1;
        prerequisites[0][1] = 0;
        prerequisites[1][0] = 0;
        prerequisites[1][1] = 1;
        System.out.println(new Problem207().canFinish(2, prerequisites));

        
        int[][] prerequisites2 = new int[1][2];
        prerequisites2[0][0] = 1;
        prerequisites2[0][1] = 0;
        System.out.println(new Problem207().canFinish(2, prerequisites2));

        // [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
        
        int[][] prerequisites3 = new int[6][2];
        prerequisites3[0][0] = 1;
        prerequisites3[0][1] = 0;

        prerequisites3[1][0] = 2;
        prerequisites3[1][1] = 6;
        
        prerequisites3[2][0] = 1;
        prerequisites3[2][1] = 7;
        
        prerequisites3[3][0] = 6;
        prerequisites3[3][1] = 4;
        
        prerequisites3[4][0] = 7;
        prerequisites3[4][1] = 0;

        prerequisites3[5][0] = 0;
        prerequisites3[5][1] = 5;
        System.out.println(new Problem207().canFinish(8, prerequisites3));
    }
}
