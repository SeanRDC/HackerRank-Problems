// ==========================================
// SET 1: PREPARING THE WORKSPACE
// ==========================================
// Let's get our environment ready to grab the input integer, n.

// Problem 1: Set up your `Solution` class.
// Problem 2: Set up your `public static void main(String[] args)` method.
// Problem 3: Import and create your `Scanner` object to read from `System.in`.
// Problem 4: Grab the integer by declaring `int n = scan.nextInt();` (and close your scanner!)


// ==========================================
// SET 2: PART 1 - THE START (INITIALIZATION)
// ==========================================
// A Java `for` loop skeleton looks like this: `for (start; stop; step) { ... }`

// Problem 5: We need to multiply `n` starting from 1 (e.g., 2 x 1, 2 x 2).
// Problem 6: In the first slot of the loop, declare an integer `i` and set it to 1.
// Problem 7: Code: `int i = 1;`
// Problem 8: Place this inside the parenthesis: `for (int i = 1; ...)`


// ==========================================
// SET 3: PART 2 - THE STOP (CONDITION)
// ==========================================
// We need to tell the loop when to stop running.

// Problem 9: The loop will keep running as long as this middle condition evaluates to TRUE.
// Problem 10: The challenge asks us to print the first 10 multiples.
// Problem 11: So we want the loop to run as long as `i` is less than or equal to 10.
// Problem 12: Code: `i <= 10;` Add it to the loop: `for (int i = 1; i <= 10; ...)`


// ==========================================
// SET 4: PART 3 - THE STEP (UPDATE)
// ==========================================
// We need to tell the loop how to change `i` after every cycle.

// Problem 13: We want `i` to go up by exactly 1 each time (1, 2, 3...).
// Problem 14: In Java, the shortcut to add 1 to a variable is `++`.
// Problem 15: Code: `i++`
// Problem 16: Complete the loop skeleton: `for (int i = 1; i <= 10; i++) { ... }`


// ==========================================
// SET 5: THE GRAND FINALE
// ==========================================
// Let's write the code inside the curly braces to do the actual math and printing.

// Problem 17: We need to calculate the result of `n * i`.
// Problem 18: We need to print it exactly matching HackerRank's format: `2 x 1 = 2`
// Problem 19: Remember, Java uses the `+` sign to glue (concatenate) text and variables together.
// Problem 20: Inside your loop's curly braces, write your print command:
// System.out.println(n + " x " + i + " = " + (n * i));
import java.util.Scanner;

public class loop1 {
    public static void main (String [] args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        scan.close();

        for (int i = 1; i <= 10; i++) {
            Systemo.out.println(n + " x " + i + " = " + (n * i));
        }
    }
}