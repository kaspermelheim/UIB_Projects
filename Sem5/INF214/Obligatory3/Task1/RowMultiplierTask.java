
package Task1;

public class RowMultiplierTask implements Runnable {

    private final double[][] C, A, B;
    private final int row;

    public RowMultiplierTask(double[][] C, double[][] A, double[][] B, int i) {
        this.C = C;

        this.A = A;
        this.B = B;

        this.row = i;
    }

    public void run() {
        for (int j = 0; j < B[0].length; j++) {
            C[row][j] = 0;
            for (int k = 0; k < A[row].length; k++)
                C[row][j] += A[row][k] * B[k][j];
        } // for j
    }
}
