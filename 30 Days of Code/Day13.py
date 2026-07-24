# ==========================================
# SET 1: THE ABSTRACT BASE CLASS (Building the Precode)
# ==========================================

# MINI-LESSON: THE 'abc' LIBRARY
# Python doesn't have Abstract Classes built into its core syntax like Java or C++. 
# To use them, we have to import a special built-in library called `abc` (Abstract Base Classes).

# Problem 1: At the very top of your file, import the tools we need.
# Write: `from abc import ABCMeta, abstractmethod`
from abc import ABCMeta, abstractmethod

# Problem 2: Define a class named `Book`. 
# To make it abstract, it needs special parameters in its parentheses. 
# Write: `class Book(object, metaclass=ABCMeta):`
class Book(object, metaclass=ABCMeta):
    
# Problem 3: Inside `Book`, define the constructor method `__init__`.
# It needs to take `self`, `title`, and `author`. 
    def __init__(self, title, author):

# Problem 4: Inside the constructor, save the two passed arguments 
# into instance variables: `self.title = title` and `self.author = author`.
        self.title = title
        self.author = author

# Problem 5 (MINI-BOSS: THE ABSTRACT METHOD):
# An abstract class needs an abstract method—a method with no body that forces child classes to do the work.
# Below your constructor, write the decorator `@abstractmethod`.
# On the very next line, define the method: `def display(self):` 
# Inside `display`, just write the word `pass`. Send this Set 1 code over for review!
    @abstractmethod
    def display(self):
        pass

# ==========================================
# SET 2: INHERITANCE (The MyBook Subclass)
# ==========================================

# MINI-LESSON: PASSING THE BATON
# Now we build the actual concrete class. Since `Book` already has an `__init__` that handles `title` and `author`, we will use `super()` to hand those variables back to the parent so we don't repeat code.

# Problem 6: Define a new class named `MyBook` that inherits from `Book`.
# Syntax: `class SubClass(BaseClass):`
class MyBook(Book):

# Problem 7: Define the `MyBook` constructor (`__init__`). 
# It needs to take `self`, `title`, `author`, AND a new trait: `price`.
    def __init__(self, title, author, price):

# Problem 8: Inside the constructor, call the parent's constructor using `super().__init__(...)`.
# Pass it the two variables the parent expects: `title` and `author`.
        super().__init__(title, author)
        self.price = price

# Problem 9: On the next line, manually save the new `price` variable to an instance variable: `self.price = price`.


# Problem 10 (MINI-BOSS: CHECK YOUR BUILDER):
# Review your `MyBook` constructor. It should take 4 parameters, use `super()` for the first two, and save the third manually. 



# ==========================================
# SET 3: FULFILLING THE ABSTRACT CONTRACT
# ==========================================

# MINI-LESSON: OVERRIDING
# Because the parent class has `@abstractmethod def display(self):`, Python will crash if we don't build our own `display` method inside `MyBook`. We have to fulfill the contract!

# Problem 11: Inside `MyBook`, below the constructor, define the method: `def display(self):`
    def display(self):

# Problem 12: Inside `display`, write a print statement using an f-string to output: "Title: {self.title}"
        print(f"Title: {self.title}")

# Problem 13: On the next line, write a print statement using an f-string to output: "Author: {self.author}"
        print(f"Author: {self.author}")

# Problem 14: On the next line, write a print statement using an f-string to output: "Price: {self.price}"
        print(f"Price: {self.price}")

# Problem 15 (MINI-BOSS: THE CONTRACT FULFILLED):
# Review your `display` method. It should consist of three clean `print` f-strings. 
# The abstract contract is now fulfilled!



# ==========================================
# SET 4: DRIVER CODE & GRAND FINALE
# ==========================================

# MINI-LESSON: TAKING INPUT
# We need to grab three separate lines of input from the user and feed them into our `MyBook` class.

# Problem 16: Outside and at the very bottom of your script, write the main execution block: 
# `if __name__ == '__main__':`


# Problem 17: Inside this block, create a variable `title` and set it equal to `input()`.
# On the next line, create `author` and set it equal to `input()`.


# Problem 18: The price needs to be a number, not a string. 
# Create a variable `price` and set it equal to `int(input())`.


# Problem 19: Instantiate your class! Create a variable called `new_novel` and set it equal to `MyBook(title, author, price)`.


# Problem 20 (THE GRAND FINALE):
# Firing the method! On the final line, call the display method on your object: `new_novel.display()`.
# YOU HAVE NOW WRITTEN THE ENTIRE SCRIPT, PRECODE AND ALL, FROM SCRATCH!


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================