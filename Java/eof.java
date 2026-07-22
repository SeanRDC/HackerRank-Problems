/* ==========================================
   BLOCK 1: THE COUNTER & THE UNKNOWN
   ==========================================
   THEORY: When you don't know exactly how many times a loop needs to run, 
   you use a `while` loop instead of a `for` loop. A `for` loop is like saying 
   "Run exactly 5 times." A `while` loop is like saying "Keep running as long 
   as this statement is true."
   
   Because a `while` loop doesn't have a built-in counter (like the `int i = 0` 
   in a `for` loop), if we want to count something, we have to manually create 
   our own counter variable OUTSIDE the loop, and update it INSIDE the loop.

   WORD PROBLEM: Write your standard imports (`java.io.*` and `java.util.*`), 
   your class wrapper, and your main method. Inside `main`, instantiate your 
   Scanner object to read from `System.in`. 
   
   The output requires us to number our lines starting at 1. Directly under your 
   scanner, create an `int` variable named `lineNumber` and initialize it to 1.
*/

/* ==========================================
   BLOCK 2: PEEKING INTO THE STREAM (HASNEXT)
   ==========================================
   THEORY: How do we know if we have reached the End Of File (EOF)? 
   The Java Scanner has a brilliant method called `hasNext()`. 
   
   Think of `hasNext()` like a periscope. It doesn't actually pull any data 
   out of the pipeline; it just peeks down the pipe. If it sees more data 
   waiting, it returns `true`. If the pipe is completely empty, it returns `false`. 
   This makes it the absolute perfect condition for a `while` loop!

   WORD PROBLEM: Create a `while` loop. For the condition inside the parentheses, 
   call the `hasNext()` method on your scanner object. (This translates to: 
   "While the scanner sees more data waiting in the pipeline, keep looping.")
*/

/* ==========================================
   BLOCK 3: READING THE WHOLE LINE (NEXTLINE)
   ==========================================
   THEORY: Inside the loop, we need to actually grab the data. But there is a trap! 
   If you use `sc.next()`, the scanner grabs a single word and stops the second 
   it sees a space. If the input is "Hello world", `sc.next()` only grabs "Hello".
   
   To grab an entire sentence, spaces and all, we must use `sc.nextLine()`. 
   This tells the scanner to read everything until it sees a hidden "Enter" 
   (newline) character.

   WORD PROBLEM: Inside your `while` loop, do the following three things:
   1. Create a `String` variable and assign it the value of `sc.nextLine()`.
   2. Print the output exactly as HackerRank requested: the `lineNumber`, 
      concatenated with a single space (" "), concatenated with your String variable.
   3. Increment your `lineNumber` variable by 1 (using the `++` shortcut) so 
      it is ready for the next cycle.
      
   Finally, outside your `while` loop, close your scanner!
*/

