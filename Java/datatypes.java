// ==========================================
// SET 1: NEW DATA TYPES
// ==========================================
// We know how to grab an integer. Now we need a decimal and a string.

// Problem 1: Set up your `Solution` class and `main` method, and create 
// your `Scanner scan = new Scanner(System.in);`

// Problem 2: Grab the integer just like last time: `int i = scan.nextInt();`

// Problem 3: In Java, a decimal is called a `double`. 
// Grab the decimal using: `double d = scan.nextDouble();`

// Problem 4: In Java, text is called a `String` (with a capital S!). 
// To grab a full line of text, we use `.nextLine()`. 
// But wait... we can't just write `String s = scan.nextLine();` yet!


// ==========================================
// SET 2: THE SCANNER TRAP (THE PROBLEM)
// ==========================================
// Let's visualize what the computer's memory (the "buffer") is doing.

// Problem 5: When you type "42" and press the Enter key, you actually send 
// TWO things to the computer: the number 42, and an invisible "Newline" character (\n).

// Problem 6: The buffer looks like this: `42\n3.1415\nWelcome to HackerRank\n`

// Problem 7: `nextInt()` is only looking for numbers. It grabs the 42, but 
// it ignores the `\n` and leaves it sitting in the buffer!

// Problem 8: `nextDouble()` grabs the 3.1415, but it ALSO leaves the next `\n` 
// sitting in the buffer!


// ==========================================
// SET 3: THE SCANNER TRAP (THE SOLUTION)
// ==========================================
// Why does this break the String?

// Problem 9: `nextLine()` works by reading everything up until it hits a `\n`. 

// Problem 10: If you run `nextLine()` immediately after `nextDouble()`, it instantly 
// hits the leftover `\n` from the previous line, assumes the line is empty, and stops!

// Problem 11: THE FIX: We have to manually clear that leftover `\n` out of the way.

// Problem 12: Directly under your `double d = scan.nextDouble();`, write a blank 
// command just to "eat" the leftover newline: `scan.nextLine();`


// ==========================================
// SET 4: GRABBING THE STRING & PRINTING
// ==========================================
// Now that the buffer is clear, we can safely grab our actual String.

// Problem 13: Now it's safe to write: `String s = scan.nextLine();`

// Problem 14: Time to print! In Python, you can use commas: `print("Int:", i)`
// In Java, you must use the plus sign (+) to join text and variables (Concatenation).

// Problem 15: Print the string: `System.out.println("String: " + s);`

// Problem 16: Print the double: `System.out.println("Double: " + d);`


// ==========================================
// SET 5: THE GRAND FINALE
// ==========================================
// Let's assemble the whole script!

// Problem 17: Remember to name your class `Solution`.

// Problem 18: Make sure your `import java.util.Scanner;` is at the very top.

// Problem 19: Print the final integer: `System.out.println("Int: " + i);`
// (Notice that HackerRank wants them printed in the reverse order you grabbed them!)

// Problem 20: Always close your scanner at the end: `scan.close();`
import java.util.Scanner;

public class datatypes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine(); // Buffer to remove the \n from the previous inputs
        String s = scan.nextLine();
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}