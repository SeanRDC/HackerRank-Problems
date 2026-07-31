# ==========================================
# SET 1: THE CONTRACT (INTERFACES & INHERITANCE)
# ==========================================

# MINI-LESSON: MOCKING INTERFACES IN PYTHON
# To create an interface in Python, we create a base class. Inside it, we define the method names we want our future subclasses to have, but we don't write any logic. Instead, we forcefully raise an error.

# Problem 1: Let's write the contract. 
# Define a base class named `AdvancedArithmetic`. Make it inherit from `(object)`.


# Problem 2: Inside this base class, define a method named `divisorSum(n)`. 
# (Note: In HackerRank's stub for this specific problem, they omitted `self` in the base class. We will follow their exact blueprint).


# Problem 3: We need to enforce the contract. If someone tries to use this base class directly without writing their own logic, it should explode. 
# Inside `divisorSum(n)`, write: `raise NotImplementedError`


# Problem 4: Now we need our actual worker class. 
# Define a new class named `Calculator` that inherits from `AdvancedArithmetic`. 
# Put `pass` inside it for now.


# Problem 5 (MASTER PROBLEM 1: THE BLUEPRINT):
# Review your code. You should have an interface class that raises an error, and an empty Calculator class that inherits from it. 
# Send Set 1 over for review, or keep going if you are in the zone!



# ==========================================
# SET 2: SATISFYING THE CONTRACT (Prep Work)
# ==========================================

# MINI-LESSON: OVERRIDING METHODS
# Because `Calculator` inherits from `AdvancedArithmetic`, it currently has a deadly `divisorSum` method that will raise an error. We must "override" it by writing our own safe version with the exact same name!

# Problem 6: Inside your `Calculator` class, delete `pass`. 
# Define the instance method: `def divisorSum(self, n):`
# (Notice we include `self` here because this is a standard instance method).


# Problem 7: We need to find all the divisors of `n` and add them up. 
# Inside the method, create a variable to keep a running total (e.g., `total`) and initialize it to 0.


# Problem 8: We have to test every number from 1 all the way up to `n` to see if it's a divisor.
# Write a `for` loop using `range()`. 
# Hint: `range(1, n)` stops just BEFORE `n`. How do you make it include `n` itself?


# Problem 9: Concept Check (No code needed).
# How do we know if a number is a "divisor"? 
# If we divide `n` by the number, the remainder must be exactly 0. We will use the modulo operator (`%`) for this!


# Problem 10 (MASTER PROBLEM 2: THE LOOP ENGINE):
# Assemble your overridden method, the tracking variable, and the loop setup. 



# ==========================================
# SET 3: THE DIVISOR LOGIC
# ==========================================

# Problem 11: Inside your `for` loop, we need to test the current loop number (let's call it `i`).
# Write an `if` statement that checks if `n` modulo `i` is exactly equal to 0.


# Problem 12: If the remainder is 0, we found a divisor! 
# Inside the `if` block, add the current number `i` to your running `total` variable.


# Problem 13: Once the loop has finished completely (un-indented back to the method level), 
# we need to hand the final answer back to whoever called the method.
# Write a `return` statement to return your running total.


# Problem 14: Concept Check (No code needed).
# Checking every number from 1 to N is a Time Complexity of O(N). For N = 1000, it loops 1000 times. There is a way to do this in O(sqrt(N)) time by finding pairs of divisors, but for this specific HackerRank challenge, O(N) is perfectly fine and much easier to read!


# Problem 15 (MASTER PROBLEM 3: THE MATH ENGINE):
# Assemble the divisibility check, the addition logic, and the return statement. Your `Calculator` class is now fully functional!



# ==========================================
# SET 4: THE DRIVER CODE (The Pre-code)
# ==========================================

# MINI-LESSON: DYNAMIC TYPE CHECKING
# HackerRank wants proof that your Calculator actually used the interface. They use `type(my_calculator).__bases__[0].__name__`. 
# This looks crazy, but it just means: "Look at the object, find its base (parent) class, and print the name of that parent class."

# Problem 16: Outside and below your classes (no indentation), 
# grab standard input, convert it to an integer, and store it in a variable named `n`.


# Problem 17: We need a worker. 
# Instantiate a new `Calculator` object and assign it to a variable named `my_calculator`.


# Problem 18: Tell the worker to do the math! 
# Call the `divisorSum` method on your calculator, pass in `n`, and save the returned result to a variable named `s`.


# Problem 19: HackerRank demands a very specific first line of output. 
# Print this exact string concatenation: 
# `print("I implemented: " + type(my_calculator).__bases__[0].__name__)`


# Problem 20 (GRAND FINALE: THE VERDICT):
# On the final line, simply `print(s)`. 
# Assemble your entire script! You have successfully built a strict interface, overridden its deadly method, implemented a math algorithm, and proven your inheritance structure!


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================