/* ==========================================
   BLOCK 1: THE STRUCTURAL SHELL (YOUR TURN!)
   ==========================================
   To master Java, you need to build muscle memory for the boilerplate.
   1. At the very top, write your imports for java.util.* and java.io.*
   2. Create your public class named Solution.
   3. Inside the class, write your standard main method signature.
   4. Inside main, initialize your Scanner object to read from System.in.
   5. Grab the first integer (let's call it 't') which tells us how many test cases there are.
   6. Create a 'for' loop that runs 't' times.
*/

/* ==========================================
   BLOCK 2: THE TRY-CATCH SAFETY NET
   ==========================================
   Inside your 'for' loop, you need a try-catch block. Why?
   Because if the grader feeds your program a massive number, it is too 
   big for even the `long` memory bucket. It overflows and the scanner crashes.
   
   1. Write a `try { ... }` block.
   2. Inside the try block, grab the massive input: `long x = sc.nextLong();`
   3. Print the starting message exactly as requested: x + " can be fitted in:"
   4. Immediately after the try block, write a `catch(Exception e) { ... }` block.
   5. Inside the catch block, the scanner crashed before grabbing the data. 
      Use `sc.next()` to grab the bad data as a String, and print it concatenated 
      with " can't be fitted anywhere."
*/

/* ==========================================
   BLOCK 3: UNDERSTANDING MEMORY BUCKETS
   ==========================================
   Now, go back inside your 'try' block (under your print statement). 
   We need to check which buckets 'x' fits in.
   * byte: The shot glass (8 bits). Holds numbers from -128 to 127.
   * short: The coffee mug (16 bits).
   * int: The pitcher (32 bits).
   * long: The water tower (64 bits).
*/

/* ==========================================
   BLOCK 4: THE BUILT-IN CONSTANTS (ASSEMBLING THE LOGIC)
   ==========================================
   To check if 'x' fits in a bucket, you COULD type out the exact max/min numbers 
   like -2147483648 to 2147483647. But one typo fails the test! 
   Instead, use Java's built-in variables: Short.MIN_VALUE, Short.MAX_VALUE, etc.
   
   1. Write an 'if' statement checking if 'x' is between -128 and 127. 
      If true, print "* byte".
   2. Write a separate 'if' statement checking if 'x' is between Short.MIN_VALUE 
      and Short.MAX_VALUE. If true, print "* short".
   3. Write a separate 'if' statement checking if 'x' is between Integer.MIN_VALUE 
      and Integer.MAX_VALUE. If true, print "* int".
   4. Because HackerRank assigned the input to a `long x`, if the code reaches 
      this point without crashing to the catch block, it inherently fits in a long! 
      No 'if' statement needed—just print "* long".
      
   Finally, outside your for loop and at the end of your main method, 
   don't forget to close your scanner!
*/