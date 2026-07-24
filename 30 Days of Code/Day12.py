# ==========================================
# SET 1: THE BASE CLASS (Building the Precode)
# ==========================================
# Before we can inherit anything, we need the parent class. Let's build the `Person` blueprint.

# Problem 1: Define a class named `Person`. Inside it, define the constructor method `__init__`.
# It needs to take four things: `self`, `firstName`, `lastName`, and `idNumber`. 
# Just put `pass` inside it for now.


# Problem 2: Delete `pass`. Inside your constructor, save the three passed arguments 
# into instance variables: `self.firstName`, `self.lastName`, and `self.idNumber`.


# Problem 3: A person should be able to introduce themselves. 
# Below your constructor, create a new instance method called `printPerson(self)`.
# Just put `pass` inside it for now.


# Problem 4: Inside `printPerson`, we need to print the name exactly like this: "Name: lastName, firstName"
# Write a print statement that outputs this string format using your instance variables.


# Problem 5 (MINI-BOSS: THE PARENT IS READY):
# Still inside `printPerson`, add a second print statement on the next line: "ID: idNumber"
# Test your class by creating `p = Person("John", "Doe", 12345)` and calling `p.printPerson()`.
# If it prints correctly, comment out your test code and keep the clean `Person` class!



# ==========================================
# SET 2: INHERITANCE (The Student Subclass)
# ==========================================
# Now we want a `Student`. A student IS A person, plus they have test scores.

# Problem 6: Define a new class named `Student` that inherits from `Person`. 
# Syntax reminder: `class SubClass(BaseClass):`


# Problem 7: Define the `Student` constructor. 
# It needs to take `self`, plus the three Person traits (`firstName`, `lastName`, `idNumber`), 
# AND a new trait: `scores` (which will be a list of integers).


# Problem 8: We don't want to rewrite the logic for saving the name and ID. The parent class already knows how!
# Inside your `Student` constructor, use the `super()` function to call the parent's `__init__`.
# Pass it the three variables `Person` requires: `firstName`, `lastName`, and `idNumber`.


# Problem 9: The `super()` call handled the first three variables. 
# Now, right below that, manually save the new `scores` list to an instance variable `self.scores`.


# Problem 10 (MINI-BOSS: TEST THE INHERITANCE):
# Create a test student: `s = Student("Jane", "Smith", 9876, [100, 80])`.
# Call `s.printPerson()`. 
# Notice how you never wrote `printPerson` inside `Student`? It inherited it! If it works, comment out your test.



# ==========================================
# SET 3: BEHAVIOR & MATH
# ==========================================
# Students need to calculate their average grade based on their scores list.

# Problem 11: Inside your `Student` class, below the constructor, define a new method: `def calculate(self):`.
# Put `pass` inside it.


# Problem 12: Inside `calculate`, we need the sum of all test scores. 
# Create a variable called `total`. Use Python's built-in `sum()` function on your `self.scores` variable.


# Problem 13: We also need to know how many tests were taken. 
# Create a variable called `count`. Use Python's built-in `len()` function on your `self.scores`.


# Problem 14: Calculate the average by dividing `total` by `count`. 
# Store this result in a variable called `a`.


# Problem 15 (MINI-BOSS: THE MATH CHECK):
# Temporarily add `print(a)` at the bottom of your `calculate` method.
# Test it: `s = Student("Test", "User", 111, [100, 80])` -> `s.calculate()`. 
# It should print `90.0`. Comment out the test code when done!



# ==========================================
# SET 4: GRADING LOGIC & DRIVER CODE (The Final Precode)
# ==========================================
# We need to turn that average `a` into a letter grade, and then write the code that actually runs the program!

# Problem 16: Remove the temporary print statement in `calculate`. 
# Look at "image_cacbda.png". If `a` is between 90 and 100 (90 <= a <= 100), `return 'O'`.
# Write this first `if` statement.


# Problem 17: Write the next two `elif` statements for grade 'E' (80 <= a < 90) and grade 'A' (70 <= a < 80).
# Make sure to return the correct characters.


# Problem 18: Finish the `calculate` method! 
# Add the `elif` for 'P' (55 <= a < 70), 'D' (40 <= a < 55), and an `else` for 'T' (a < 40).


# Problem 19: Now for the driver code! (This is what HackerRank usually hides).
# Outside and at the very bottom of your script, write: `if __name__ == '__main__':`
# Inside this block, use `input().split()` to read the first line of user input. 
# Save the first item as `firstName`, the second as `lastName`, and the third as `idNum`.


# Problem 20 (THE GRAND FINALE):
# Finish the driver code! 
# 1. Read the next line (number of scores) using `int(input())` but we can just ignore saving it.
# 2. Read the third line of scores. Use `list(map(int, input().split()))` to turn the string of numbers into a list of integers. Save it as `scores`.
# 3. Create a `Student` object using all these inputs.
# 4. Call `printPerson()` on your object.
# 5. Print `"Grade:"` followed by the result of `calculate()`.
# YOU HAVE NOW WRITTEN THE ENTIRE SCRIPT FROM SCRATCH!


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================
# (Copy all your working pieces from above and put them together here into one beautiful, finished file).