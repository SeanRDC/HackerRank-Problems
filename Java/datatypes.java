// Reads an int, a double, and a full line of text with Scanner, consuming the leftover
// newline before the string, then prints them in reverse order.

import java.util.Scanner;

public class datatypes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}