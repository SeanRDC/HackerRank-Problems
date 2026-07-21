// ==========================================
// SET 1: THE MODULO OPERATOR (ODD VS EVEN)
// ==========================================
// To solve this, we first need to know how to check if a number is odd or even.

// Problem 1: In Java, just like Python, the modulo operator `%` gives you the remainder of division.
// Problem 2: If a number is even, dividing it by 2 leaves a remainder of 0: `n % 2 == 0`
// Problem 3: If a number is odd, dividing it by 2 leaves a remainder of 1: `n % 2 != 0` (or == 1)
// Problem 4: We will use `n % 2 != 0` as our very first condition to catch all odd numbers.


// ==========================================
// SET 2: JAVA IF-ELSE SYNTAX
// ==========================================
// Let's learn how to structure conditional statements in Java.

// Problem 5: In Python, you write `if condition:`. 
// In Java, the condition MUST be in parentheses: `if (condition)`

// Problem 6: In Python, the code block is indented.
// In Java, the code block MUST be wrapped in curly braces: `{ ... }`

// Problem 7: In Python, you write `elif`. 
// In Java, you write `else if`.

// Problem 8: The structure looks like this:
// if (condition) {
//     // code
// } else if (other_condition) {
//     // code
// }


// ==========================================
// SET 3: LOGICAL "AND"
// ==========================================
// We need to check if a number is both EVEN *and* IN A SPECIFIC RANGE.

// Problem 9: In Python, you can chain conditions like `2 <= n <= 5`. 
// In Java, THIS IS ILLEGAL. You must evaluate each side separately!

// Problem 10: In Python, you join conditions with the word `and`.
// In Java, you join them with the double ampersand symbol: `&&`

// Problem 11: To check if `n` is between 2 and 5 (inclusive), you MUST write:
// `n >= 2 && n <= 5`

// Problem 12: So, to check if a number is even AND between 2 and 5, you write:
// `n % 2 == 0 && n >= 2 && n <= 5`


// ==========================================
// SET 4: MAPPING OUT THE LOGIC
// ==========================================
// Let's translate the HackerRank instructions into Java conditions.

// Problem 13: CONDITION 1 - "If n is odd, print Weird"

// Problem 14: CONDITION 2 - "If n is even and in the inclusive range of 2 to 5, print Not Weird"

// Problem 15: CONDITION 3 - "If n is even and in the inclusive range of 6 to 20, print Weird"

// Problem 16: CONDITION 4 - "If n is even and greater than 20, print Not Weird"



// ==========================================
// SET 5: THE GRAND FINALE
// ==========================================
// Let's put it all together inside the boilerplate!

// Problem 17: Set up your class, your `main` method, and your `Scanner` to read 
// the integer `n`. (Review the last challenge if you need a refresher!)

// Problem 18: Write the `if` statement for Condition 1. Use `System.out.println("Weird");`

// Problem 19: Write the `else if` statements for Conditions 2, 3, and 4, printing 
// the correct exact text for each.

// Problem 20: Remember to close your scanner (`scan.close();`) at the very end!
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
