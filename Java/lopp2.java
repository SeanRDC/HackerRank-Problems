// For each query, starts from a and keeps adding 2^j * b for j from 0 to n - 1,
// printing the running total after every step.

import java.util.*;

class loop2{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();

        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int currentResult = a;

            for (int j = 0; j < n; j++) {
                currentResult += ((int) Math.pow(2, j) * b);
                System.out.print(currentResult + " ");
            }

        System.out.println();
        }
        in.close();
    }
}