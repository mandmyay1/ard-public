// https://leetcode.com/problems/invert-binary-tree/description/
/*
 * Given the root of a binary tree, invert the tree, and return its root.
 */

public class Problem226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) { return root; }

        TreeNode left = root.left;
        TreeNode right = root.right;

        root.left = right;
        root.right = left;

        invertTree(left);
        invertTree(right);

        return root;
    }
}
