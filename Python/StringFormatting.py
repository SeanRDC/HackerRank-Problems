# ==========================================
# SET 1: THE BUILT-IN CONVERTERS (New Concept)
# ==========================================
# Python has built-in functions to convert integers into other number bases. 
# However, they return strings with prefixes attached to them.

# Problem 1: Print `bin(17)`. 
# Expected Output: 0b10001 (The '0b' stands for binary).
print(bin(17))

# Problem 2: Print `oct(17)`.
# Expected Output: 0o21 (The '0o' stands for octal).
print(oct(17))

# Problem 3: Print `hex(17)`.
# Expected Output: 0x11 (The '0x' stands for hexadecimal).
print(hex(17))

# ==========================================
# SET 2: CLEANING THE STRINGS
# ==========================================
# We need the numbers, but HackerRank doesn't want those prefixes. 
# You already learned how to slice strings in the Mutations challenge!

# Problem 4: Use string slicing to chop off the first two characters of `bin(17)`. Print it.
# Expected Output: 10001
print(bin(17)[2:])

# Problem 5: Slice off the first two characters of `oct(17)`. Print it.
# Expected Output: 21
print(oct(17)[2:])

# Problem 6: Slice off the first two characters of `hex(17)`. Print it.
# Expected Output: 11
print(hex(17)[2:])

# Problem 7: HackerRank specifically asks for CAPITALIZED hex values (e.g., 'a' becomes 'A').
# Take your sliced hex string from Problem 6 and chain your uppercase string method to it. Print it.
print(hex(17)[2:].upper())

# ==========================================
# SET 3: FINDING THE MASTER WIDTH
# ==========================================
# The prompt says: "Each value should be space-padded to match the width of the binary value of N."

# Problem 8: Create a variable `N = 17`.
N = 17

# Problem 9: Generate the clean (sliced) binary string for `N`. Save it to `max_bin`.
max_bin = bin(N)[2:]

# Problem 10: Find the length of `max_bin`. Save it to a variable called `width` and print it.
# Expected Output: 5
width = len(max_bin)
print(width)

# ==========================================
# SET 4: FORMATTING WITH RJUST
# ==========================================
# Now that we know our width is 5, we can use the `.rjust()` method you mastered in the Logo challenge.

# Problem 11: Set a test variable `i = 1`. 
# Convert `i` to a string, and right-justify it using your `width` variable. Print it.
# Expected Output:     1  (four spaces, then the 1)
i = 1
a = str(i).rjust(width)

# Problem 12: Get the clean octal string for `i`. Right-justify it using `width`. Print it.
b = str(oct(i)[2:]).rjust(width) # the oct hex bin already returns a string but for safety still wrapped them in str

# Problem 13: Get the clean, uppercase hex string for `i`. Right-justify it using `width`. Print it.
c = str(hex(i)[2:].upper()).rjust(width)

# Problem 14: Get the clean binary string for `i`. Right-justify it using `width`. Print it.
d = str(bin(i)[2:]).rjust(width)

# Problem 15: Print all four formatted strings on a single line. 
# Hint: If you pass multiple variables to `print(a, b, c, d)`, Python automatically puts one space between them!
print(a, b, c, d)

# ==========================================
# SET 5: THE F-STRING SUPERPOWER (New Concept)
# ==========================================
# Slicing and `.rjust()` works perfectly! But modern Python (3.6+) added a superpower.
# F-strings have built-in base converters AND padding tools, meaning you can skip `bin()`, `oct()`, 
# and `.rjust()` entirely. 
# Syntax: f"{value:>{width}base}"
# base = 'd' (decimal), 'o' (octal), 'X' (uppercase hex), 'b' (binary)

# Problem 16: Let's test the binary conversion. Print `f"{i:b}"`. 
# (Notice it converts to binary WITHOUT the '0b' prefix!)

# Problem 17: Let's add the dynamic padding. Print `f"{i:>{width}b}"`.
# Expected Output:     1  (binary 1, right-justified in a width of 5)

# Problem 18: Do the same thing, but format it as uppercase hex using 'X'. Print it.

# Problem 19: Do the same thing, but format it as octal using 'o'. Print it.


# ==========================================
# SET 6: THE GRAND FINALE
# ==========================================
# You now have TWO different ways to solve this: The `.rjust()` method or the f-string method. 

# Problem 20: Complete the HackerRank function.
# 1. Calculate your dynamic `width` using the binary version of `number`.
# 2. Write a `for` loop that goes from 1 up to `number` (inclusive!).
# 3. Inside the loop, print the four values separated by spaces, correctly aligned.

def print_formatted(number):
    # Your logic here!
    pass

# Test it:
# print_formatted(17)