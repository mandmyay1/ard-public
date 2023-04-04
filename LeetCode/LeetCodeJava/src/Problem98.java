// https://leetcode.com/problems/validate-binary-search-tree/description/
/*
 * Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 */

public class Problem98 {
    public boolean isValidBST(TreeNode root) {
        if (root == null) { return true; }
        if (root.left == null && root.right == null) {
            return true;
        }
        int currentVal = root.val;
        if (root.right != null) {
            int minOfRight = findMin(root.right);
            if (currentVal >= minOfRight) {
                return false;
            }
        }
        if (root.left != null) {
            int maxOfLeft = findMax(root.left);
            if (currentVal <= maxOfLeft) {
                return false;
            }
        }
        return isValidBST(root.left) && isValidBST(root.right);
    }

    public int findMin(TreeNode root) {
        if (root.left == null) {
            return root.val;
        }
        return findMin(root.left);
    }
    public int findMax(TreeNode root) {
        if (root.right == null) {
            return root.val;
        }
        return findMax(root.right);
    }
}
