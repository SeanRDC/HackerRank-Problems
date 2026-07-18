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

# MOCK INPUT: 
# S = "Hacker"

# Problem 5: Write a loop that iterates over the indices of `S` using `range()` and `len()`.
list_length = len(S)
for i in range(list_length):
# Problem 6: Inside the loop, write a conditional statement to check if the current index is even.
    if i % 2 == 0:
# Problem 7: If the index is even, append the character at that index to your `even_chars` string.
        even_chars += S[i]
# Problem 8: Add an alternative block. If the index is odd, append the character to your `odd_chars` string.
    else:
        odd_chars += S[i]
# Problem 9: Outside the loop, print both strings combined with a space in between them.
# EXPECTED OUTPUT: 
# Hce akr
print(f'{even_chars} {odd_chars}')

# Problem 10: Reflect on the fact that this took several lines of code. It works perfectly, 
# but Python has a secret weapon to do this instantly.


# ==========================================
# SET 3: THE SLICING SUPERPOWER (THE EASY WAY)
# ==========================================
# Remember slicing: `[start : stop : step]`. If we leave `start` and `stop` blank, 
# Python automatically uses the beginning and end of the string.

# Problem 11: Using string slicing with a step of 2, grab all the even-indexed characters 
# starting from the beginning of `S` and print them.
# EXPECTED OUTPUT: 
# Hce 
print(S[0::2])

# Problem 12: Now let's grab the odd indices. Using string slicing, start at index 1 
# and step by 2 to grab all the odd-indexed characters. Print them.
# EXPECTED OUTPUT: 
# akr
print(S[1::2])

# Problem 13: Combine both slices into a single print statement. 
# (Hint: Pass them as two separate arguments to the print function so it automatically adds a space!)
# EXPECTED OUTPUT: 
# Hce akr
print(S[0::2], S[1::2])

# MOCK INPUT UPDATE:
# S = "Rank"
S = "Rank"

# Problem 14: Try it with the second test string. 
# Update `S` to "Rank" and run the exact same print statement from Problem 13 again.
# EXPECTED OUTPUT: 
# Rn ak
print(S[0::2], S[1::2])

# ==========================================
# SET 4: HANDLING HACKERRANK'S TEST CASES
# ==========================================
# HackerRank adds a new layer here: The first input is a number `T` representing 
# how many strings we need to process.

# MOCK INPUT:
# T = 2
T = 2

# Problem 16: Create a mock variable `T` for the number of test cases and set it to 2.

# Problem 17: Write a loop that runs `T` times. 
# (Pro-tip: use `_` as your loop variable instead of `i` when you just need the loop to count).
for _ in range(T):

# Problem 18: Inside the loop, create a mock input `S` set to "Hacker". 
# On the next line, print the sliced even and odd characters just like you did in Set 3.
# EXPECTED OUTPUT:
# Hce akr
# Hce akr
    S = "Hacker"
    print(S[0::2], S[1::2])

# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's write the exact code that HackerRank wants. No mock variables!

# TERMINAL MOCK INPUT (What you will type when you run the code):
# 2
# Hacker
# Rank

# Problem 19: Get the integer input for `T` from the user.
T = int(input())

# Problem 20: Write the final loop that runs `T` times. 
# Inside, get the string input from the user and immediately print its even and odd slices.
for _ in range(T):
    user_input = input()
    print(user_input[0::2], user_input[1::2])

# TERMINAL EXPECTED OUTPUT:
# Hce akr
# Rn ak