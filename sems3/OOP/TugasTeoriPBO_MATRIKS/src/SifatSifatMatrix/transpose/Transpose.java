package SifatSifatMatrix.transpose;

public class Transpose {
    public static int[][] transposeMatrix(int[][] original) {
        int rows = original.length;
        int cols = original[0].length;
        int[][] transpose = new int[cols][rows];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transpose[j][i] = original[i][j];
            }
        }

        return transpose;
    }
}

