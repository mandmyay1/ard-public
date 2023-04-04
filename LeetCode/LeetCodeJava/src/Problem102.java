// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
/*
 * Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 */

import java.util.ArrayList;
import java.util.List;

public class Problem102 {
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) { return result; }

        List<TreeNode> queue = new ArrayList<TreeNode>();
        queue.add(root);
        levelOrderHelper(queue);
        return result;
    }
    private void levelOrderHelper(List<TreeNode> queue) {
        if (queue.size() == 0) { return; }

        List<TreeNode> nextLevel = new ArrayList<TreeNode>();
        List<Integer> thisLevelResult = new ArrayList<Integer>();

        while (queue.size() > 0) {
            TreeNode nd = queue.get(0);
            queue.remove(0);
            
            thisLevelResult.add(nd.val);
            if (nd.left != null) {
                nextLevel.add(nd.left);
            }
            if (nd.right != null) {
                nextLevel.add(nd.right);
            }
        }
        result.add(thisLevelResult);

        levelOrderHelper(nextLevel);
    }
}
