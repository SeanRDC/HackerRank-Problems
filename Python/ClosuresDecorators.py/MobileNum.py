# ==============================================================================
# FUNDAMENTALS CURRICULUM: DECORATORS & DATA SANITIZATION
# ==============================================================================
# Goal: Write the inner function `fun(l)` that intercepts a raw list of strings.
# It must extract the last 10 digits of each string, format them properly, 
# and then pass the cleaned list to the original function `f`.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: ISOLATING THE CORE NUMBER (SLICING)
# ---------------------------------------------------------

# Problem 1: The Variable Prefix Problem
# Concept: The inputs are a mess. They might start with "0", "91", "+91", or 
# nothing at all. This means string lengths could be 10, 11, 12, or 13 characters!

# Problem 2: The Anchor Point
# Concept: While the prefixes change, one rule NEVER changes: the actual phone 
# number is always exactly the LAST 10 digits of the string.

# Problem 3: Negative Slicing
# Concept: In Python, a negative slice like `string[-3:]` grabs exactly the 
# last 3 characters of a string, no matter how long the string is. What negative 
# slice will grab the last 10 characters?
# Mock Input 1: "07895462130" -> Slice -> "7895462130"
# Mock Input 2: "+919875641230" -> Slice -> "9875641230"
phone1 = "07895462130"[-10:]
print(phone1)
phone2 = "+919875641230"[-10:]
print(phone2)
# ---------------------------------------------------------
# CONCEPT BLOCK 2: FORMATTING THE STRING
# ---------------------------------------------------------

# Problem 4: The First Chunk
# Concept: Now that you have the clean 10-digit string, you need the first 5 
# digits. You can use standard positive slicing: `string[0:5]`.

# Problem 5: The Second Chunk
# Concept: Grab the last 5 digits using positive slicing: `string[5:10]` (or 
# just `string[5:]`).

# Problem 6: The Final Concatenation
# Concept: Use an f-string or string addition to combine them into the required 
# format: "+91 {chunk_1} {chunk_2}".
# Mock Input: "7895462130" 
# Mock Output: "+91 78954 62130"
print(f"+91 {phone1[:5]} {phone1[5:]}")
# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE DECORATOR ENGINE
# ---------------------------------------------------------

# Problem 7: The Inner Function `fun(l)`
# Concept: The parameter `l` is the raw list of unformatted phone numbers from 
# the boilerplate.

# Problem 8: The Transformation Loop
# Concept: You need to apply the logic from Concept Blocks 1 & 2 to every item 
# in `l`. You can do this using a standard `for` loop to build a new list, or 
# even better, a List Comprehension!
# Mock Syntax: `clean_list = [your_formatting_logic for number in l]`

# Problem 9: The Handoff (The Most Important Step)
# Concept: Now that you have `clean_list`, you must pass it to the original 
# function! Look at the top of the decorator: `def wrapper(f):`. 
# `f` represents `sort_phone`. 

# Problem 10: Triggering the Original Function
# Concept: The very last line of your `fun(l)` block should execute `f`, passing 
# `clean_list` into it as the argument.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Stage ---
# Boilerplate reads Integer N = 3
# Boilerplate loops 3 times, building list `l`.
# l = ["07895462130", "919875641230", "9195969878"]

# --- The Interception ---
# Boilerplate attempts to call `sort_phone(l)`.
# The `@wrapper` intercepts it.
# The `wrapper` passes `l` into your `fun(l)` method instead!

# --- The Sanitization (Inside `fun`) ---
# Index 0: "07895462130" -> Grabs last 10 -> "7895462130" -> Formats -> "+91 78954 62130"
# Index 1: "919875641230" -> Grabs last 10 -> "9875641230" -> Formats -> "+91 98756 41230"
# Index 2: "9195969878" -> Grabs last 10 -> "9195969878" -> Formats -> "+91 91959 69878"
# `clean_list` is fully constructed.

# --- The Handoff ---s
# `fun` executes `f(clean_list)`.
# `sort_phone` finally wakes up! It receives the clean list, sorts it, and prints it.
def wrapper(f):
    def fun(l):
        new_list = []
        for i in l:
            clean = i[-10:]
            new_list.append(f"+91 {clean[:5]} {clean[5:]}")
        return f(new_list)
        # or much more optimized version (one liner)
        #return f([(f"+91 {i[-10:][:5]} {i[-10:][5:]}") for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
