public class Problem79 {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (existsFromPoint(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    private boolean existsFromPoint(char[][] board, String word, int x, int y, int wordPointer) {
        // Base case, the string has been used up entirely
        if (wordPointer >= word.length()) { return true; }

        // Outside the bounds of the board
        if (x >= board.length || x < 0) { return false; }
        if (y >= board[0].length || y < 0) { return false; }

        char wordAt = word.charAt(wordPointer);
        char boardChar = board[x][y];
        if (wordAt == boardChar) {
            board[x][y] = '&';

            // Could be from (x-1,y), (x+1, y), (x, y+1), (x, y-1)
            boolean above = existsFromPoint(board, word, x, y + 1, wordPointer + 1);
            if (above) { return above; }
            boolean below = existsFromPoint(board, word, x, y - 1, wordPointer + 1);
            if (below) { return below; }
            boolean right = existsFromPoint(board, word, x + 1, y, wordPointer + 1);
            if (right) { return right; }
            boolean left = existsFromPoint(board, word, x - 1, y, wordPointer + 1);
            if (left) { return left; }

            board[x][y] = boardChar;
        }
        return false;
    }


    public static void main(String[] args) {
        char[][] board = new char[3][4];
        board[0][0] = 'A';
        board[0][1] = 'B';
        board[0][2] = 'C';
        board[0][3] = 'E';
        board[1][0] = 'S';
        board[1][1] = 'F';
        board[1][2] = 'C';
        board[1][3] = 'S';
        board[2][0] = 'A';
        board[2][1] = 'D';
        board[2][2] = 'E';
        board[2][3] = 'E';
        String word = "ABCCED";

        System.out.println(new Problem79().exist(board, word));
        System.out.println(new Problem79().exist(board, "ABCB"));
    }
}
