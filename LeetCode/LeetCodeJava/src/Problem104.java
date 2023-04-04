// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
/**
 * Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 */

public class Problem104 {
    public int maxDepth(TreeNode root) {
        if (root == null) { return 0; }
        
        int depthRight = maxDepth(root.right);
        int depthLeft = maxDepth(root.left);

        return 1 + Math.max(depthRight, depthLeft);
    }
}
