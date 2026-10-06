// Reads n and prints 'Weird' or 'Not Weird' depending on whether n is odd or even and
// which range it falls in.

import java.util.Scanner;

public class ifelse {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        if (n % 2 != 0) {
            System.out.print("Weird");
        } else if (n % 2 == 0 && (n >= 2 && n <= 5)) {
            System.out.print("Not Weird");
        } else if (n % 2 == 0 && (n >= 6 && n <= 20)) {
            System.out.println("Weird");
        } else if (n % 2 == 0 && n > 20) {
            System.out.println("Not Werid");
        }
    }
}
