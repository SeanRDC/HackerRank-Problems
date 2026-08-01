# ==========================================
# SET 1: THE CONTRACT (INTERFACES)
# ==========================================

# MINI-LESSON: MOCKING INTERFACES IN PYTHON
# Python doesn't have an `interface` keyword. We simulate it by creating a base class with methods that intentionally crash if you don't overwrite them. This forces any child class to strictly follow the blueprint.

# Problem 1: Define a base class named `AdvancedArithmetic`. 
# Make it inherit from `(object)` explicitly: `class AdvancedArithmetic(object):`


# Problem 2: Inside this base class, define a method named `divisorSum(n)`. 
# (Note: HackerRank intentionally omitted `self` here to simulate a pure interface blueprint).


# Problem 3: Enforce the contract! 
# Inside `divisorSum(n)`, write: `raise NotImplementedError`


# Problem 4: Define your worker class named `Calculator` that inherits from `AdvancedArithmetic`. 
# Put `pass` inside it for now.


# Problem 5 (MASTER PROBLEM 1: THE BLUEPRINT):
# Review your code. You have built a strict interface that raises an error, and an empty Calculator class that inherits from it. Send Set 1 over for review, or keep pushing!



# ==========================================
# SET 2: OVERRIDING THE METHOD
# ==========================================

# MINI-LESSON: OVERRIDING
# Because `Calculator` inherits from `AdvancedArithmetic`, it currently possesses that deadly `divisorSum` method. We must "override" it by writing our own functioning version with the exact same name.

# Problem 6: Inside your `Calculator` class, delete `pass`. 
# Override the method by defining: `def divisorSum(self, n):`


# Problem 7: Create a variable to keep a running total of our divisors and initialize it to 0.


# Problem 8: We need to test every number from 1 all the way up to `n`.
# Write a `for` loop using `range()`. 
# Hint: `range(1, n)` stops just BEFORE `n`. How do you make it include `n` itself?


# Problem 9: Concept Check (No code needed).
# To find a "divisor", we check if `n` divided by our loop number has a remainder of exactly 0. We use the modulo operator (`%`) for this!


# Problem 10 (MASTER PROBLEM 2: THE LOOP ENGINE):
# Assemble your overridden method, the tracking variable, and the loop setup. 



# ==========================================
# SET 3: THE DIVISOR LOGIC
# ==========================================

# Problem 11: Inside your `for` loop, let's test the current loop number (e.g., `i`).
# Write an `if` statement checking if `n` modulo `i` is exactly equal to 0.


# Problem 12: If it equals 0, we found a divisor! 
# Inside the `if` block, add the current number to your running total variable.


# Problem 13: Once the loop has finished completely (un-indented back to the method level), 
# `return` your running total.


# Problem 14: Concept Check (No code needed).
# Checking every number from 1 to N gives this algorithm a Time Complexity of O(N). If N = 1000, it loops 1000 times. This is perfectly efficient for this challenge!


# Problem 15 (MASTER PROBLEM 3: THE MATH ENGINE):
# Assemble the divisibility check, the addition logic, and the return statement. 



# ==========================================
# SET 4: THE DRIVER CODE (Dynamic Checking)
# ==========================================

# MINI-LESSON: DYNAMIC TYPE CHECKING
# HackerRank wants absolute proof that your Calculator actually inherited from the interface. 
# They use `type(my_calculator).__bases__[0].__name__`. 
# This translates to: "Look at the object, find its base (parent) class at index 0, and print that parent's name."

# Problem 16: Outside your classes, grab standard input, convert it to an integer, and store it in `n`.


# Problem 17: Instantiate a new `Calculator` object and assign it to `my_calculator`.


# Problem 18: Call the `divisorSum` method on your calculator, pass in `n`, and save the result to `s`.


# Problem 19: Prove your inheritance! 
# Print this exact string concatenation: 
# `print("I implemented: " + type(my_calculator).__bases__[0].__name__)`


# Problem 20 (GRAND FINALE: THE VERDICT):
# On the final line, print your sum variable `s`. 
# Assemble your entire script! 


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================