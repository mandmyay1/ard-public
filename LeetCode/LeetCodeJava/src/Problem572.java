// https://leetcode.com/problems/subtree-of-another-tree/description/
/*
 * Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
 */

public class Problem572 {
    
    private boolean isDirectSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) { 
            return true;
        }
        if (root == null && subRoot != null) { 
            return false;
        }
        if (root != null && subRoot == null) {
            return false;
        }
        // If the values match and the subtrees match, it's a valid subtree
        if (root.val == subRoot.val) {
            if (isDirectSubtree(root.left, subRoot.left) && isDirectSubtree(root.right, subRoot.right)) {
                return true;
            }
        }
        return false;
    }
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) { 
            return true;
        }
        if (root == null && subRoot != null) { 
            return false;
        }
        if (root != null && subRoot == null) {
            return false;
        }
        // If the values match and the subtrees match, it's a valid subtree
        if (isDirectSubtree(root, subRoot)) {
            return true;
        }
        // Could find the subtree down on the left or right side
        if (isSubtree(root.left, subRoot)) {
            return true;
        }
        if (isSubtree(root.right, subRoot)) {
            return true;
        }
        return false;
    }
}
