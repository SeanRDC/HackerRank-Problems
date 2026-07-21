# ==========================================
# SET 1: UNDERSTANDING THE MATH
# ==========================================
# Let's map out how a factorial actually works.

# Problem 1: Mathematically, 3! means 3 * 2 * 1. 
# Problem 2: Notice that 2 * 1 is just 2!. 
# Problem 3: Therefore, 3! is the exact same thing as 3 * 2!. 
# Problem 4: This gives us our recursive formula: factorial(n) = n * factorial(n - 1)


# ==========================================
# SET 2: THE BASE CASE (THE BRAKES)
# ==========================================
# If a function calls itself forever, Python will crash with a "RecursionError".
# We MUST tell it when to stop. This is called the Base Case.

# Problem 5: Start defining your function: `def factorial(n):`
def factorial(n):

# Problem 6: What is the lowest factorial we care about? Mathematically, 1! is 1. 
# (And 0! is also 1). So our stopping point is when `n` reaches 1.

# Problem 7: Inside your function, write an `if` statement to check if `n <= 1`.
    if n <= 1:
# Problem 8: If it is, simply `return 1`. (This stops the function from calling itself again!)
        return 1

# ==========================================
# SET 3: THE RECURSIVE CASE (THE ENGINE)
# ==========================================
# If we haven't hit the bottom yet, we need to call the function again.

# Problem 9: Under your `if` block, write an `else:` block.
    else:
# Problem 10: Inside the `else` block, we need to return `n` multiplied by the factorial of `n - 1`.
        return n * factorial(n - 1)
# Problem 11: Write `return n * factorial(n - 1)`. 
# (Yes, you are using the function's name inside of its own definition! That is recursion.)
    
# Problem 12: Double check your indentation. The `if/else` should be cleanly aligned inside the function.


# ==========================================
# SET 4: TRACING THE CALL STACK
# ==========================================
# Let's trace what your code does when you run `factorial(3)`.

# Problem 13: You pass in 3. Since 3 > 1, it hits the else block and returns `3 * factorial(2)`.
# But wait, it doesn't know what `factorial(2)` is yet! So Python pauses and runs it.
print(factorial(3))

# Problem 14: `factorial(2)` hits the else block and returns `2 * factorial(1)`.
# Python pauses again.
print(factorial(2))

# Problem 15: `factorial(1)` hits the `if n <= 1:` Base Case! It simply returns `1`.
print(factorial(1))

# Problem 16: Now Python unwinds the paused tasks backwards: 
# It knows `factorial(1)` is 1. So `2 * 1 = 2`. 
# Now it knows `factorial(2)` is 2. So `3 * 2 = 6`. It returns 6!


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's plug it into HackerRank's boilerplate.

# Problem 17: Look at the starter code HackerRank provided in your prompt.
# Find the empty `def factorial(n):` block.
def factorial(n):

# Problem 18: Put your `if` Base Case inside it.
# Problem 19: Put your `else` Recursive Case inside it.
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Problem 20: DO NOT touch any of the code under `if __name__ == '__main__':`. 
# HackerRank wrote that so their automatic testing system can pass values into your function and read the result.