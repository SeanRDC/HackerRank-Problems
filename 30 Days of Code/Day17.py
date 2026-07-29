# ==========================================
# SET 1: THE CLASS & METHOD SHELL
# ==========================================

# MINI-LESSON: CREATING YOUR OWN RULES
# We are building a class that does math. But we have a strict rule: No negative numbers allowed!
# If a user breaks this rule, we won't try to fix it. We will "raise" an exception and force the program to stop.

# Problem 1: Define a new class named `Calculator`.
# (No need to inherit anything this time, just a standard class).


# Problem 2: Notice that the problem does not ask us to store any variables when the Calculator is created.
# This means we do NOT need an `__init__` constructor! 


# Problem 3: Inside the class, define the instance method: `def power(self, n, p):`


# Problem 4: Just put the word `pass` inside the method for now.


# Problem 5 (MINI-BOSS: THE SHELL IS READY):
# Review your class. It should just be the `Calculator` definition and the empty `power` method. 
# Send Set 1 over for review!



# ==========================================
# SET 2: CHECKING THE RULE & RAISING EXCEPTIONS
# ==========================================

# MINI-LESSON: THE 'RAISE' KEYWORD
# In Python, we use the `raise` keyword to manually trigger an error. 
# For example: `raise Exception("You broke the rules!")` will instantly crash the program and print that exact message, UNLESS someone catches it with a `try/except` block.

# Problem 6: Delete `pass`. Inside your `power` method, write an `if` statement to check our rule.
# Check if `n` is less than 0 OR if `p` is less than 0. 
# (Hint: use the `or` keyword).


# Problem 7: Inside that `if` block, we need to throw our error.
# Type the keyword `raise`.


# Problem 8: Right after `raise`, create the exception object with our exact required message.
# Write: `Exception("n and p should be non-negative")`
# (Make sure the spelling and capitalization match exactly).


# Problem 9: Concept Check (No code needed). 
# When a `raise` statement is triggered, the method instantly stops running. It acts like a brutal `return`. 
# Because of this, we don't actually need an `else:` block for the math. If the numbers are negative, the program explodes here and never reaches the math anyway!


# Problem 10 (MINI-BOSS: THE TRAP IS SET):
# Review your `if` statement and `raise` logic. You have successfully built a tripwire for negative numbers!



# ==========================================
# SET 3: DOING THE MATH
# ==========================================

# MINI-LESSON: EXPONENTS IN PYTHON
# If the code survives the `if` statement without raising an exception, it means both numbers are positive!
# We just need to calculate n to the power of p.
# In Python, you can use the `**` operator (e.g., `2 ** 3` is 8).

# Problem 11: Below your `if` block (un-indented so it is not inside the `if`), 
# calculate the result of `n` to the power of `p`. 


# Problem 12: You don't even need to save this to a variable. 
# Just use the `return` keyword to return the result of that math directly.


# Problem 13: Concept Check (No code needed).
# Notice how clean this is? We check for bad data at the very top. If it's bad, we throw an error and escape. If it's good, we just do the math and return it. This is a very standard professional coding pattern.


# Problem 14: (No code needed).
# Ensure your indentation is correct. The `return` statement should be at the same indentation level as your `if` statement.


# Problem 15 (MINI-BOSS: THE METHOD IS COMPLETE):
# Your `power` method is finished! It guards against negatives and processes the positives perfectly.



# ==========================================
# SET 4: WRITING THE DRIVER CODE (The Pre-code)
# ==========================================

# MINI-LESSON: CATCHING WHAT WE THROW
# Now we build the outside world that actually uses our Calculator. 

# Problem 16: Outside the class at the bottom of the file (no indentation), instantiate your class!
# Create a variable `myCalculator` and set it equal to `Calculator()`.
# On the next line, read the number of test cases: `T = int(input())`


# Problem 17: Create a `for` loop that runs `T` times: `for i in range(T):`
# Inside the loop, read the two numbers using Python's mapping trick: 
# `n, p = map(int, input().split())`


# Problem 18: Now we try the dangerous code. Still inside the loop, write a `try:` block.
# Inside the `try` block, calculate the answer: `ans = myCalculator.power(n, p)`
# On the next line, `print(ans)`.


# Problem 19: But what if our Calculator throws that exception from Set 2? We must catch it!
# Below the `try` block, write the catch block: `except Exception as e:`
# Inside it, just print the exception: `print(e)`
# (This takes the custom message we wrote in Set 2 and prints it safely to the screen).


# Problem 20 (THE GRAND FINALE):
# Assemble your full script! The Calculator class with the tripwire, and your beautifully written driver code that safely catches the explosion.


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================