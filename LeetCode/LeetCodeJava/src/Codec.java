import java.util.ArrayList;
import java.util.List;

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<String> sb = new ArrayList<String>();
        List<TreeNode> queue = new ArrayList<TreeNode>();
        queue.add(root);
        serializeHelper(queue, sb);
        return String.join(",", sb);
    }
    private void serializeHelper(List<TreeNode> queue, List<String> sb) {
        while (!queue.isEmpty()) {
            TreeNode nd = queue.get(0);
            queue.remove(0);
            
            if (nd == null) {
                sb.add("null");
            } else {
                sb.add(Integer.toString(nd.val));
                queue.add(nd.left);
                queue.add(nd.right);
            }
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] splitData = data.split(",");
        List<TreeNode> queue = new ArrayList<TreeNode>();
        if (splitData.length == 0 || splitData[0].equals("null")) {
            return null;
        }
        TreeNode root = new TreeNode(Integer.parseInt(splitData[0]));
        queue.add(root);
        for (int i = 1; i < splitData.length && !queue.isEmpty(); i += 2) {
            TreeNode currentParentNd = queue.get(0);
            queue.remove(0);

            String leftText = splitData[i];
            if (!leftText.equals("null")) {
                TreeNode leftNd = new TreeNode(Integer.parseInt(leftText));
                currentParentNd.left = leftNd;
                queue.add(leftNd);
            }
            if (i + 1 < splitData.length) {
                String rightText = splitData[i + 1];
                if (!rightText.equals("null")) {
                    TreeNode rightNd = new TreeNode(Integer.parseInt(rightText));
                    currentParentNd.right = rightNd;
                    queue.add(rightNd);
                }
            }
        }
        return root;
    }
}