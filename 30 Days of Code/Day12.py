# ==========================================
# SET 1: THE BASE CLASS (Building the Precode)
# ==========================================

# MINI-LESSON: CLASSES, __init__, AND self
# - What is a class? A class is a blueprint. It doesn't represent a specific person, but rather the *idea* of a person. 
# - What is __init__? It stands for "initialize". This is a special function called a "constructor". The absolute millisecond you create a new Person, Python runs __init__ automatically to build them.
# - What is self? Imagine you have a blueprint for a house. `self` is like saying "MY front door", "MY roof". It tells Python to attach data specifically to the object being created, not just floating around in the void. Every function inside a class must take `self` as its first parameter!

# Problem 1: Define a class named `Person`. Inside it, define the constructor method `__init__`.
# It needs to take four things: `self`, `firstName`, `lastName`, and `idNumber`. 
# Just put `pass` inside it for now.
class Person:
    def __init__(self, firstName, lastName, idNumber):

# Problem 2: Delete `pass`. Inside your constructor, save the three passed arguments 
# into instance variables using `self` (e.g., `self.firstName = firstName`). This takes the temporary data passed in and permanently attaches it to the object.
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        
# Problem 3: A person should be able to introduce themselves. 
# Below your constructor, create a new instance method called `printPerson(self)`.
# (Notice how it also needs `self`? That's so it can look up its own name later!). Just put `pass` inside it for now.
    def printPerson(self):

# Problem 4: Inside `printPerson`, we need to print the name exactly like this: "Name: lastName, firstName"
# Write a print statement that outputs this string format using your instance variables (`self.lastName` and `self.firstName`).
        print(f"Name: {self.lastName}, {self.firstName}")

# Problem 5 (MINI-BOSS: THE PARENT IS READY):
# Still inside `printPerson`, add a second print statement on the next line: "ID: idNumber" (using `self.idNumber`).
# Test your class by creating a test variable outside the class: `p = Person("John", "Doe", 12345)` 
# Then call `p.printPerson()`. If it prints correctly, comment out your test code!
        print(f"ID: {self.idNumber}")

p = Person("John", "Doe", 12345)
p.printPerson()


# ==========================================
# SET 2: INHERITANCE (The Student Subclass)
# ==========================================

# MINI-LESSON: INHERITANCE AND super()
# - What is Inheritance? Sometimes blueprints share things. A Student IS A Person. Instead of copying and pasting the Person code, we tell Python: "Make a Student, but give them everything a Person has too."
# - What is super()? When we give a Student their own `__init__`, we accidentally overwrite the Person's `__init__`. To fix this, we use `super()`. It literally means "Go up to my parent class (Person) and run their code really quick."

# Problem 6: Define a new class named `Student` that inherits from `Person`. 
# Syntax: `class SubClass(BaseClass):`
class Student(Person):

# Problem 7: Define the `Student` constructor (`__init__`). 
# It needs to take `self`, plus the three Person traits (`firstName`, `lastName`, `idNumber`), 
# AND a new trait: `scores` (which will be a list of integers).
    def __init__(self, firstName, lastName, idNumber, scores):

# Problem 8: We don't want to rewrite the logic for saving the name and ID. The parent class already knows how!
# Inside your `Student` constructor, use the `super()` function to call the parent's `__init__`.
# Syntax: `super().__init__(arg1, arg2, arg3)` 
# Pass it the three variables `Person` requires: `firstName`, `lastName`, and `idNumber`.
        super().__init__(firstName, lastName, idNumber)

# Problem 9: The `super()` call handled the first three variables. 
# Now, right below that, manually save the new `scores` list to an instance variable `self.scores`.
        self.scores = scores

# Problem 10 (MINI-BOSS: TEST THE INHERITANCE):
# Create a test student: `s = Student("Jane", "Smith", 9876, [100, 80])`.
# Call `s.printPerson()`. 
# Notice how you never wrote `printPerson` inside `Student`? It inherited it! If it works, comment out your test.


# ==========================================
# SET 3: BEHAVIOR & MATH
# ==========================================

# MINI-LESSON: INSTANCE METHODS
# Just like `printPerson`, we can create any action we want our object to perform. 
# Because we saved `self.scores` in the constructor, any method we write inside the Student class can access those scores!

# Problem 11: Inside your `Student` class, below the constructor, define a new method: `def calculate(self):`.
# Put `pass` inside it.
    def calculate(self):

# Problem 12: Inside `calculate`, we need the sum of all test scores. 
# Create a variable called `total`. Use Python's built-in `sum()` function on your `self.scores` variable.
        total = sum(self.scores)

# Problem 13: We also need to know how many tests were taken. 
# Create a variable called `count`. Use Python's built-in `len()` function on your `self.scores`.
        count = len(self.scores)

# Problem 14: Calculate the average by dividing `total` by `count`. 
# Store this result in a variable called `a`.
        a = total / count
        print(a)
# Problem 15 (MINI-BOSS: THE MATH CHECK):
# Temporarily add `print(a)` at the bottom of your `calculate` method.
# Test it: `s = Student("Test", "User", 111, [100, 80])` -> `s.calculate()`. 
# It should print `90.0`. Comment out the test code when done!
s = Student("Test", "User", 111, [100, 80])
s.calculate()


# ==========================================
# SET 4: GRADING LOGIC & DRIVER CODE
# ==========================================

# MINI-LESSON: THE DRIVER CODE
# - `if __name__ == '__main__':` tells Python: "Only run the code below if I am running THIS specific file directly."
# - `input().split()` waits for the user to type something, then splits it into a list based on spaces.
# - `map(int, ...)` is a cool trick that takes a list of strings (like ["100", "80"]) and turns them all into integers.

# Problem 16: Remove the temporary print statement in `calculate`. 
# Look at "image_cacbda.png". If `a` is between 90 and 100 ($90 \le a \le 100$), `return 'O'`.
# Write this first `if` statement. (Hint: Python allows chaining like `if 90 <= a <= 100:`)


# Problem 17: Write the next two `elif` statements for grade 'E' ($80 \le a < 90$) and grade 'A' ($70 \le a < 80$).
# Make sure to return the correct characters.


# Problem 18: Finish the `calculate` method! 
# Add the `elif` for 'P' ($55 \le a < 70$), 'D' ($40 \le a < 55$), and an `else` for 'T' ($a < 40$).


# Problem 19: Now for the driver code! (This is what HackerRank usually hides).
# Outside and at the very bottom of your script (no indentation), write: `if __name__ == '__main__':`
# Inside this block, use `input().split()` to read the first line of user input. 
# Save the first item (index 0) as `firstName`, the second (index 1) as `lastName`, and the third (index 2) as `idNum`.


# Problem 20 (THE GRAND FINALE):
# Finish the driver code inside the `if __name__` block! 
# 1. Read the next line (number of scores) using `int(input())` but we can just ignore saving it.
# 2. Read the third line of scores. Use `list(map(int, input().split()))` to turn the string of numbers into a list of integers. Save it as `scores`.
# 3. Create a `Student` object using all these inputs (firstName, lastName, idNum, scores).
# 4. Call `printPerson()` on your object.
# 5. Print `"Grade: "` followed by the result of `calculate()`.


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================