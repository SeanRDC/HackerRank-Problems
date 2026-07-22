/* ==========================================
   BLOCK 1: THE BOILERPLATE & SCANNER
   ==========================================
   THEORY: Java requires strict structure. Every program needs imported tools, 
   a class wrapper, and a main method where the code actually starts running. 
   To read user input, we instantiate a Scanner object: `Scanner scanName = new Scanner(System.in);`
   
   WORD PROBLEM: Import the `java.util.*` and `java.io.*` libraries. 
   Create a public class named `Solution`. Inside it, create the standard 
   `public static void main(String []args)` method. Inside the main method, 
   create a Scanner object named `sc` to read standard input. Grab the very 
   first integer from the scanner and store it in an `int` variable named `t`.
*/

/* ==========================================
   BLOCK 2: THE FOR LOOP
   ==========================================
   THEORY: A Java `for` loop gives you microscopic control over the iteration. 
   It has three parts separated by semicolons: (1) Where to start, (2) When 
   to stop, and (3) How to count. 
   Example: `for (int i = 0; i < 5; i++) { ... }`
   
   WORD PROBLEM: The integer `t` you just grabbed represents the number of 
   test cases HackerRank will throw at you. Write a `for` loop that initializes 
   an integer `i` at 0, runs as long as `i` is less than `t`, and increments 
   `i` by 1 each cycle.
*/

/* ==========================================
   BLOCK 3: THE TRY-CATCH TRAPDOOR
   ==========================================
   THEORY: A `try-catch` block protects your program from violently crashing. 
   If you try to put a massive number into a `long` using `sc.nextLong()`, 
   and the number is too big for 64-bit memory, the Scanner panics. 
   The code inside `try { ... }` instantly stops, and the program falls 
   through the trapdoor into the `catch (Exception e) { ... }` block.
   
   WORD PROBLEM: Inside your `for` loop, create a try-catch block. 
   Inside the `try` section, grab the next long integer from the scanner and 
   save it in a `long` variable named `x`. Directly below that, print `x` 
   concatenated with the exact text " can be fitted in:" to the console.
*/

/* ==========================================
   BLOCK 4: CLEARING THE BUFFER (THE CATCH BLOCK)
   ==========================================
   THEORY: When `sc.nextLong()` fails, the massive bad text doesn't disappear; 
   it stays stuck inside the Scanner! If we don't remove it, the loop will 
   crash again on the next cycle. The command `sc.next()` reads data as a 
   String (text). A String can be infinitely long, so it safely acts like a 
   vacuum, sucking up the massive bad number.
   
   WORD PROBLEM: Inside the `catch` section, the scanner has just crashed. 
   Grab the massive string from the scanner using `sc.next()` and print it 
   concatenated with the exact text " can't be fitted anywhere."
*/

/* ==========================================
   BLOCK 5: THE MEMORY BUCKETS (SEQUENTIAL IF'S)
   ==========================================
   THEORY: To check if a number fits inside a bucket, we check if it is 
   greater than or equal to the minimum, AND (`&&`) less than or equal to 
   the maximum. Java has built-in constants so you don't have to memorize 
   the exact numbers: `Short.MIN_VALUE`, `Integer.MAX_VALUE`, etc. 
   (Note: We use independent `if` statements, NOT `else if`, because a tiny 
   number can fit into multiple buckets at the same time!)
   
   WORD PROBLEM: Go back inside your `try` block, right under your print statement.
   1. Write an `if` statement checking if `x` is >= -128 AND <= 127. 
      If true, print "* byte".
   2. Write an `if` statement checking if `x` is between `Short.MIN_VALUE` 
      and `Short.MAX_VALUE`. If true, print "* short".
   3. Write an `if` statement checking if `x` is between `Integer.MIN_VALUE` 
      and `Integer.MAX_VALUE`. If true, print "* int".
   4. Finally, since the program successfully saved the input to the `long x` 
      variable without crashing, we already know it fits! Without writing any 
      `if` statement at all, simply print "* long".
*/

/* ==========================================
   BLOCK 6: CLEANUP
   ==========================================
   THEORY: Scanners consume memory and keep an open stream to the operating 
   system. It is a strict best practice to close them when you are done.
   
   WORD PROBLEM: Outside of your `for` loop, at the very bottom of your 
   `main` method, close your scanner using `.close()`. 
*/

import java.util.*;


public class dataypes2 {
    public static void main (String [] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for(int i = 0; i < t; i++) {
            try {
                long x = sc.nextLong();
                System.out.println(x + " can be fitted in:");
                if (x >= -128 && x <= 127) {
                    System.out.println("* byte");
                }
                if (x >= Short.MIN_VALUE && x <= Short.MAX_VALUE) {
                    System.out.println("* short");
                }
                if (x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE) {
                    System.out.println("* int");
                }
                System.out.println("* long");

            } catch (Exception e) {
                System.out.println(sc.next() + " can't be fitted anywhere.");
            }
        }
    sc.close();
    }
}