
package Task1;

import java.util.*;

public class Main {


  // random matrices
  public static double[][] generate(int rows, int columns) {
    double[][] ret = new double[rows][columns];
    Random random = new Random();
    for (int i = 0; i < rows; i++)
      for (int j = 0; j < columns; j++)
        ret[i][j] = random.nextDouble() * 10;
    return ret;
  }

  public static void main(String[] args) {

    final int size = 1000;
    double[][] matrix1 = generate(size, size);
    double[][] matrix2 = generate(size, size);
    double[][] result = new double[matrix1.length][matrix2[0].length];

    System.out.println("Serial version running...");
    Date start = new Date();
    SerialMult.multiply(matrix1, matrix2, result);
    Date end = new Date();
    System.out.println("Serial Multiplication: " + (end.getTime() - start.getTime()) + "ms");

    System.out.println("Parallel version by row running...");
    start = new Date();
    MatrixMult.multiply(matrix1, matrix2, result);
    end = new Date();
    System.out.println("Parallel Row: "+ (end.getTime() - start.getTime()) + "ms");
  }
}
