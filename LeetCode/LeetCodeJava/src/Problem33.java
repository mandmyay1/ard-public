public class Problem33 {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int middle = (right + left) / 2;

        while (middle != left && middle != right) {
            int valLeft = nums[left];
            int valRight = nums[right];
            int valMid = nums[middle];

            if (valRight <= valMid) {
                if (target <= valRight || target >= valMid) {
                    left = middle;
                }
                else {
                    right = middle;
                }
            }
            else if (valLeft >= valMid) {
                if (target <= valRight && target >= valMid) {
                    left = middle;
                }
                else {
                    right = middle;
                }
            }
            else if (valLeft < valMid) {
                if (target >= valLeft && target <= valMid) {
                    right = middle;
                }
                else {
                    left = middle;
                }
            }
            middle = (right + left) / 2;
        }

        if (nums[left] == target) { return left; }
        if (nums[right] == target) { return right; }

        return -1;
    }
    public static void main(String[] args) {
        System.out.println(new Problem33().search(new int[] {5,1,2,3,4}, 1));
        System.out.println(new Problem33().search(new int[] {4,5,6,7,8,1,2,3}, 8));
        System.out.println(new Problem33().search(new int[] {4,5,6,7,8,1,2,3}, 2));
        System.out.println(new Problem33().search(new int[] {4,5,6,7,0,1,2}, 0));
        System.out.println(new Problem33().search(new int[] {0,1,2,4,5,6,7}, 2));
        System.out.println(new Problem33().search(new int[] {0,1,2,4,5,6,7}, 3));
        System.out.println(new Problem33().search(new int[] {3,4,5,1,2}, 5));
        System.out.println(new Problem33().search(new int[] {11,13,15,17}, 17));
        System.out.println(new Problem33().search(new int[] {1}, 0));
        System.out.println(new Problem33().search(new int[] {1}, 1));
    }
}
