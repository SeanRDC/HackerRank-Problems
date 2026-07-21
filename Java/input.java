// ==========================================
// SET 1: PREPARING THE WORKSPACE
// ==========================================
// In Java, tools that aren't part of the absolute core language must be imported.

// Problem 1: At the very top of your file (before the class), import the Scanner 
// tool by writing: `import java.util.Scanner;`

// Problem 2: Create your class blueprint: `public class Solution {`

// Problem 3: Create your starting engine: `public static void main(String[] args) {`

// Problem 4: Remember how printing uses `System.out`? Taking input from the 
// keyboard uses the exact opposite stream: `System.in`.


// ==========================================
// SET 2: BUILDING THE SCANNER OBJECT
// ==========================================
// We need to create our Scanner and connect it to the keyboard stream.

// Problem 5: Inside `main`, declare a new variable of type `Scanner` named `scan`.

// Problem 6: Use the `new` keyword to build the object. 
// Syntax: `Scanner scan = new Scanner(...);`

// Problem 7: Inside the parentheses, pass `System.in` so the Scanner knows 
// where to listen for data.

// Problem 8: End the line with a semicolon! 


// ==========================================
// SET 3: READING THE DATA
// ==========================================
// HackerRank is going to pass us three integers. In Java, you must declare 
// the data type (int) before the variable name.

// Problem 9: Create an integer variable `a` and assign it the next integer 
// from the scanner: `int a = scan.nextInt();`

// Problem 10: `nextInt()` actually pauses the program, waits for the user to 
// type a number, and grabs it.

// Problem 11: Create a second integer variable: `int b = scan.nextInt();`

// Problem 12: Create a third integer variable: `int c = scan.nextInt();`


// ==========================================
// SET 4: CLEANING UP MEMORY
// ==========================================
// When you open a stream in Java (like listening to the keyboard or opening a file), 
// it locks up a tiny piece of your computer's memory.

// Problem 13: Good Java developers always close their streams when they are done.
// Problem 14: HackerRank won't fail you if you forget, but it is a vital habit!

// Problem 15: Close your scanner by writing: `scan.close();`

// Problem 16: Check your indentation. Ensure all of this is inside your `main` method.


// ==========================================
// SET 5: THE GRAND FINALE
// ==========================================
// We captured the three integers! Now we just have to spit them back out.

// Problem 17: Write a `System.out.println()` command to print variable `a`.

// Problem 18: On the next line, do the same for variable `b`.

// Problem 19: On the next line, do the same for variable `c`.

// Problem 20: Make sure every single command ends with a semicolon, and make 
// sure you have two closing curly braces `}` at the bottom of your file 
// (one to close `main`, one to close `Solution`). {
import java.util.Scanner;
    
public class input {
    public static void main (String [] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        scan.close();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
