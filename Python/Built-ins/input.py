# ==============================================================================
# FUNDAMENTALS CURRICULUM: THE EVAL() FUNCTION & DYNAMIC EXECUTION
# ==============================================================================
# Goal: Read 'x' and 'k' from a string, read a mathematical polynomial as a 
# raw string, dynamically evaluate that string as Python code, and check if 
# the result equals 'k'.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: UNDERSTANDING EVAL()
# ---------------------------------------------------------

# Problem 1: The Math String
# Concept: Create a mock string representing basic math. 
# `math_str = "10 + 5 * 2"`

# Problem 2: The Literal Print
# Concept: If you just `print(math_str)`, it prints the literal text.
# To do the math, wrap it in the `eval()` function: `eval(math_str)`. Print it.
# Mock Output: 20

# Problem 3: The Variable String
# Concept: `eval()` is powerful because it checks your current namespace for 
# variables! Create a string with a variable `x`.
# `poly_str = "x**2 + x + 1"`

# Problem 4: The Execution Context
# Concept: Above your `poly_str` variable, declare `x = 1`. 
# Now, print `eval(poly_str)`. 
# Mock Output: 3 
# (Python saw 'x' in the string, found 'x' in your code, and substituted it!)

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE SECURITY WARNING (THEORY)
# ---------------------------------------------------------

# Problem 5: The Danger of Eval
# Concept: Never use `eval()` on user input in a production application! 
# If a user inputs `"__import__('os').system('rm -rf /')"`, `eval()` will 
# literally execute the command to delete your entire hard drive. 

# Problem 6: HackerRank Sandbox
# Concept: We only use `eval()` here because HackerRank specifically designed 
# the problem around it. It is perfectly safe in this isolated sandbox.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: PARSING THE FIRST LINE
# ---------------------------------------------------------

# Problem 7: The First Mock Input
# Concept: Create a string representing the first line of HackerRank input.
# `line1 = "1 4"`

# Problem 8: The Split
# Concept: Call `.split()` on `line1` to break it into a list of strings.
# Mock Output: ['1', '4']

# Problem 9: The Map
# Concept: Wrap your split command in `map(int, ...)` to convert the strings 
# into integers.

# Problem 10: Unpacking 'x' and 'k'
# Concept: Unpack the mapped integers directly into variables `x` and `k`.
# Mock Output: x = 1, k = 4

# ---------------------------------------------------------
# CONCEPT BLOCK 4: EVALUATING THE POLYNOMIAL
# ---------------------------------------------------------

# Problem 11: The Second Mock Input
# Concept: Create a string representing the polynomial input.
# `line2 = "x**3 + x**2 + x + 1"`

# Problem 12: Evaluating the Polynomial
# Concept: Pass `line2` into `eval()` and assign the result to a variable `P`.
# Since `x` is currently set to 1 from Problem 10, this will work perfectly!

# Problem 13: Checking the Output
# Concept: Print `P`.
# Mock Output: 4

# ---------------------------------------------------------
# CONCEPT BLOCK 5: BOOLEAN COMPARISON
# ---------------------------------------------------------

# Problem 14: The Equality Operator
# Concept: We need to know if our evaluated polynomial `P` is exactly equal 
# to our target integer `k`. Write `P == k` and assign it to `result`.

# Problem 15: Printing the Boolean
# Concept: Print `result`.
# Mock Output: True (Because 4 == 4)

# Problem 16: The One-Liner Comparison
# Concept: You don't need a `result` variable or an `if/else` block! 
# `print(P == k)` will evaluate the math and instantly print True or False.

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 17: Reading x and k
# Concept: Swap out the mock string. Write a single line of code that reads 
# `input()`, splits it, maps to `int`, and unpacks into `x` and `k`.

# Problem 18: Reading the Polynomial
# Concept: Do NOT split the second line! Read it using `input()` and assign 
# it directly to `poly_str`.

# Problem 19: The Direct Print
# Concept: Inside your `print()` statement, evaluate `poly_str` and check if 
# it equals `k` using the `==` operator.

# Problem 20: Clean Code Execution
# Concept: Assemble your final script. It can easily be done in exactly 3 lines 
# of code!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Line 1 ---
# input() receives string: "1 4"
# split() breaks it: ["1", "4"]
# map() casts them: [1, 4]
# Unpacking assigns: x = 1, k = 4

# --- Input Line 2 ---
# input() receives string: "x**3 + x**2 + x + 1"
# Assigns to variable: poly_str = "x**3 + x**2 + x + 1"

# --- The Evaluation Engine ---
# eval("x**3 + x**2 + x + 1") executes.
# Python checks namespace, finds x = 1.
# Executes: 1**3 + 1**2 + 1 + 1
# Evaluates to: 4

# --- The Boolean Comparison ---
# Compares evaluated result (4) to k (4).
# 4 == 4 evaluates to: True

# --- Final Output ---
# Console Prints: True