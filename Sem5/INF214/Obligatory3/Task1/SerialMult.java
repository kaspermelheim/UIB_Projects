
package Task1;

public class SerialMult {
    public static void multiply(double[][] A, double[][] B, double[][] C) {
        int m = A.length;
        int n = A[0].length;
        int k = B[0].length;
        for (int I = 0; I < m; I++)
            for (int J = 0; J < k; J++) {
                C[I][J] = 0;
                for (int K = 0; K < n; K++)
                    C[I][J] += A[I][K] * B[K][J];
            } // for J
    }
}

