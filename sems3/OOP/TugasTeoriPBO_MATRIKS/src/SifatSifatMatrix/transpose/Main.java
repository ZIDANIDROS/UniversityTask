package SifatSifatMatrix.transpose;

public class Main {
    public static void main(String[] args) {
        int original[][] = {{1, 3, 4}, {2, 4, 3}, {3, 4, 5}};

        System.out.println("Printing Matrix without transpose:");
        printMatrix(original);

        int transpose[][] = Transpose.transposeMatrix(original);

        System.out.println("Printing Matrix After Transpose:");
        printMatrix(transpose);

        
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
