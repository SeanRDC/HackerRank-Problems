# ==========================================
# SET 1: STRING INDEXING REFRESHER
# ==========================================
# Let's set up our test case and manually grab the characters.

# Problem 1: Create a test string `S` set to "Hacker".
S = "Hacker"

# Problem 2: Print the character at index 0, index 2, and index 4. 
# (Expected Output: H, c, e)
a = S[0]
b = S[2]
c = S[4]
print(f'{a}, {b}, {c}')

# Problem 3: Print the character at index 1, index 3, and index 5.
# (Expected Output: a, k, r)
a = S[1]
b = S[3]
c = S[5]
print(f'{a}, {b}, {c}')

# Problem 4: Create two empty string variables: `even_chars` and `odd_chars`.
even_chars = ""
odd_chars = ""

# ==========================================
# SET 2: THE LOOP METHOD (THE HARD WAY)
# ==========================================
# Let's use a standard loop and modulo math to sort the characters.

# Problem 5: Write a loop that iterates over the indices of `S` using `range()` and `len()`.

# Problem 6: Inside the loop, write a conditional statement to check if the current index is even.

# Problem 7: If the index is even, append the character at that index to your `even_chars` string.

# Problem 8: Add an alternative block. If the index is odd, append the character to your `odd_chars` string.

# Problem 9: Outside the loop, print both strings combined with a space in between them.
# Expected Output: Hce akr

# Problem 10: Reflect on the fact that this took several lines of code. It works perfectly, 
# but Python has a secret weapon to do this instantly.


# ==========================================
# SET 3: THE SLICING SUPERPOWER (THE EASY WAY)
# ==========================================
# Remember slicing: `[start : stop : step]`. If we leave `start` and `stop` blank, 
# Python automatically uses the beginning and end of the string.

# Problem 11: Using string slicing with a step of 2, grab all the even-indexed characters 
# starting from the beginning of `S` and print them.
# Expected Output: Hce 

# Problem 12: Now let's grab the odd indices. Using string slicing, start at index 1 
# and step by 2 to grab all the odd-indexed characters. Print them.
# Expected Output: akr

# Problem 13: Combine both slices into a single print statement. 
# (Hint: Pass them as two separate arguments to the print function so it automatically adds a space!)
# Expected Output: Hce akr

# Problem 14: Try it with the second test string. 
# Change `S` to "Rank" and run the print statement from Problem 13 again.
# Expected Output: Rn ak

# Problem 15: Marvel at how the multi-line loop just became a single line of code.


# ==========================================
# SET 4: HANDLING HACKERRANK'S TEST CASES
# ==========================================
# HackerRank adds a new layer here: The first input is a number `T` representing 
# how many strings we need to process.

# Problem 16: Create a mock variable `T` for the number of test cases and set it to 2.

# Problem 17: Write a loop that runs `T` times. 
# (Pro-tip: use `_` as your loop variable instead of `i` when you just need the loop to count, 
# but don't actually need to use the number inside the block).

# Problem 18: Inside the loop, create a mock input `S` set to "Hacker". 
# On the next line, print the sliced even and odd characters just like you did in Set 3.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's write the exact code that HackerRank wants. No mock variables!

# Problem 19: Get the integer input for `T` from the user.

# Problem 20: Write the final loop that runs `T` times. 
# Inside, get the string input from the user and immediately print its even and odd slices.

# (For testing in your IDE, when you run it, type '2', hit enter, type 'Hacker', 
# hit enter, type 'Rank', hit enter).