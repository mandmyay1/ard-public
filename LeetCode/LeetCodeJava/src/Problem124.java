public class Problem124 {
    int globalMax = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxPathSumHelper(root);
        return globalMax;
    }
    public int maxPathSumHelper(TreeNode root) {
        if (root == null) { return 0; }
        
        int sumLeft = maxPathSumHelper(root.left);
        int sumRight = maxPathSumHelper(root.right);

        int poss0 = root.val;
        int poss1 = sumLeft + root.val;
        int poss2 = sumRight + root.val;
        int poss3 = sumRight + sumLeft + root.val;

        int temp = Math.max(poss0, poss1);
        temp = Math.max(temp, poss2);
        temp = Math.max(temp, poss3);

        globalMax = Math.max(globalMax, temp);

        int maxIncludingRoot = Math.max(poss0, poss1);
        maxIncludingRoot = Math.max(maxIncludingRoot, poss2);
        System.out.println("for " + poss0 + " poss1=" + poss1 + " poss2=" + poss2 + " poss3=" + poss3 + " globalMax=" + globalMax + " maxIncludingRoot=" + maxIncludingRoot);
        return maxIncludingRoot;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        System.out.println(new Problem124().maxPathSum(root));
    }
}
