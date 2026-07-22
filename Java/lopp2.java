// ==========================================
// SET 1: THE OUTER LOOP & THE ACCUMULATOR
// ==========================================
// HackerRank already gave you the outer loop: `for(int i = 0; i < t; i++)`
// This loops through the total number of queries so you don't have to.

// Problem 1: Inside the outer loop, you already grab the variables `a`, `b`, and `n`.
// Problem 2: We need to keep a running total for our math series. 
// Problem 3: The series always starts with `a` as the base.
// Problem 4: Directly under `int n = in.nextInt();`, declare a new integer called 
// `currentResult` and set it equal to `a`. (e.g., `int currentResult = a;`)


// ==========================================
// SET 2: THE NESTED LOOP
// ==========================================
// Now we need to generate `n` numbers for this specific query.

// Problem 5: We need a second loop inside the first one to handle the `n` terms.
// Problem 6: Create an inner `for` loop. Since we already used `i` for the outer 
// loop, standard practice is to use `j` for the inner loop.
// Problem 7: Set `j` to start at 0: `for (int j = 0; ...`
// Problem 8: Set the condition to run `n` times: `for (int j = 0; j < n; ...`
// Problem 9: Increment `j` by 1 each time: `for (int j = 0; j < n; j++) { ... }`


// ==========================================
// SET 3: MATH EXPONENTS & TYPE CASTING
// ==========================================
// We need to calculate (2^j * b) and add it to our running total.

// Problem 10: In Java, you cannot use the `^` symbol for exponents. 
// Problem 11: You must use the built-in Math library: `Math.pow(base, exponent)`
// Problem 12: To calculate 2 to the power of j, you write: `Math.pow(2, j)`
// Problem 13: THE TRAP: `Math.pow()` always returns a decimal (a `double`), but 
// HackerRank wants integers!
// Problem 14: You must force the decimal back into an integer by "casting" it.
// Problem 15: Put `(int)` in front of the math: `(int) Math.pow(2, j)`


// ==========================================
// SET 4: UPDATING THE RUNNING TOTAL
// ==========================================
// Let's add this math to our `currentResult`.

// Problem 16: Multiply your newly casted exponent by `b`: `((int) Math.pow(2, j) * b)`
// Problem 17: Inside the inner loop, add this value to `currentResult`. 
// Problem 18: Code: `currentResult += ((int) Math.pow(2, j) * b);`


// ==========================================
// SET 5: THE GRAND FINALE (PRINTING)
// ==========================================
// HackerRank is very specific: print all numbers on ONE line, separated by spaces.

// Problem 19: If you use `System.out.println()`, every number goes on a new line.
// Instead, use `.print()` to keep them on the same line, and concatenate a space:
// `System.out.print(currentResult + " ");` (Put this inside the inner loop!)

// Problem 20: Once the inner `j` loop finishes, we need to hit "Enter" before the 
// next query starts. OUTSIDE the `j` loop, but INSIDE the `i` loop, add a blank 
// `System.out.println();`

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