// ==========================================
// SET 1: THE JAVA CLASS
// ==========================================
// In Java, absolutely everything must live inside a "Class". 

// Problem 1: Look at the boilerplate provided by HackerRank: `public class Solution`
// Problem 2: `public` means this class can be accessed from anywhere.
// Problem 3: `class` is the keyword declaring a new object/blueprint.
// Problem 4: `Solution` is the name of the class. In Java, the name of your file 
// MUST exactly match the name of the public class (e.g., Solution.java).

// ==========================================
// SET 2: THE MAIN METHOD (THE ENGINE)
// ==========================================
// When you run a Java program, it aggressively searches for one specific method 
// to start the program. 

// Problem 5: Look at: `public static void main(String[] args)`
// Problem 6: `static` means the program can run this method without needing to 
// create a "Solution" object first.
// Problem 7: `void` means this method will not return any value at the end.
// Problem 8: `main` is the strict, unchangeable name the computer looks for to 
// begin executing your code.


// ==========================================
// SET 3: PRINTING TO THE CONSOLE
// ==========================================
// Python uses `print()`. Java uses a longer path.

// Problem 9: `System` is a built-in Java class that talks to your computer.
// Problem 10: `.out` is the standard output stream (your console/terminal).
// Problem 11: `.print()` prints text. 
// Problem 12: `.println()` prints text AND automatically presses "Enter" (adds a new line) 
// at the end. We will use `println()` for this challenge!

// ==========================================
// SET 4: JAVA SYNTAX LAWS
// ==========================================
// Coming from Python, these two rules are the most common ways to break your code.

// Problem 13: In Python, you can use single quotes ('Hello') or double quotes ("Hello") 
// for strings. In Java, you MUST use double quotes for strings: "Hello"
// Problem 14: Single quotes in Java are strictly reserved for single characters: 'A'
// Problem 15: In Python, a new line marks the end of a command.
// Problem 16: In Java, you MUST put a semicolon (;) at the very end of every command.


// ==========================================
// SET 5: THE GRAND FINALE
// ==========================================
// Let's write the actual code!

// Problem 17: Find the space inside the `main` method curly braces `{ ... }` 
// in the HackerRank editor.

// Problem 18: Write your first command using `System.out.println()`.

// Problem 19: Inside the parentheses, pass the exact string: "Hello, World." 
// (Don't forget the semicolon at the end of the line!)

// Problem 20: On the very next line, write a second `System.out.println()` 
// command passing the exact string: "Hello, Java." (Again, end with a semicolon!)
public class print {
    public static void main (String [] args){
        System.out.println("Hello, World.");
        System.out.println("Hello, Java");
    }
}