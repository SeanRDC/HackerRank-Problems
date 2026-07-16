# ==========================================
# SET 1: THE BLUEPRINT AND THE BUILDER (__init__)
# ==========================================
# A Class is a blueprint. 
# `__init__` is the constructor—the function that runs automatically the moment you build a new object.

# Problem 1: Create a simple class called `Dog`. Inside it, put the word `pass` (which just means "do nothing").
# Instantiate it by writing `my_dog = Dog()`. Print `my_dog`. 
# Expected Output: <__main__.Dog object at 0x...> (It prints a memory address!)
class Dog:
    pass

my_dog = Dog()
print(my_dog)

# Problem 2: Delete `pass`. Add the constructor: `def __init__(self):`. 
# Inside the constructor, `print("A dog was born!")`. 
# Run `my_dog = Dog()`. 
# Expected Output: A dog was born!
class Dog:
    def __init__(self):
        print("A dog was born!")

my_dog = Dog()

# Problem 3: Let's pass data into the constructor. 
# Update it to `def __init__(self, name):`. Inside, `print(name)`. 
# Run `my_dog = Dog("Fido")`.
# Expected Output: Fido
class Dog:
    def __init__(self, name):
        print(name)

my_dog = Dog("Fido")

# Problem 4: Printing the name is nice, but we need to SAVE it inside the object so we can use it later.
# We do this using `self`. Inside `__init__`, delete the print statement and write `self.name = name`.
# Run `my_dog = Dog("Fido")`. Then, outside the class, print `my_dog.name`.
# Expected Output: Fido
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Fido")
print(my_dog.name)

# Problem 5 (MINI-BOSS: COMBINE 1-4):
# Create the `Person` class. 
# Add the constructor: `def __init__(self, initialAge):`. 
# Inside it, save `initialAge` to an instance variable called `self.age`.
# Create `p = Person(10)` and print `p.age`.
# Expected Output: 10
class Person:
    def __init__(self, initialAge):
        self.age = initialAge

p = Person(10)
print(p.age)
# ==========================================
# SET 2: CONSTRUCTOR LOGIC
# ==========================================
# We can put `if / else` logic directly inside `__init__` to validate our data before saving it!

# Problem 6: Inside your `Person` constructor, add an `if` statement before you save the age.
# If `initialAge < 0`, print `"Too young!"`.
# Test it with `p = Person(-5)`.
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Too Young!')

p = Person(-5)

# Problem 7: If `initialAge < 0`, we don't just want to print a warning. We want to force the age to be valid.
# Inside that same `if` block, set `self.age = 0`. 
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Too Young!')
            self.age = 0

p = Person(-5)

# Problem 8: Add an `else` block. If `initialAge` is NOT less than 0, set `self.age = initialAge`.
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Too Young!')
            self.age = 0
        else:
            self.age = initialAge
            print(initialAge)

# Problem 9: Test your logic! 
# Create `p1 = Person(-5)`. Print `p1.age`. (Should print "Too young!" and then 0).
# Create `p2 = Person(15)`. Print `p2.age`. (Should just print 15).
p1 = Person(-5)
p2 = Person(15)

# Problem 10 (MINI-BOSS: HACKERRANK INIT):
# Update your `__init__` method to match the exact HackerRank requirements.
# If `< 0`: print `"Age is not valid, setting age to 0."` and set `self.age = 0`.
# Else: set `self.age = initialAge`.
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
            print(initialAge)

# ==========================================
# SET 3: INSTANCE METHODS (BEHAVIOR)
# ==========================================
# Methods are just functions that live inside a class. They MUST take `self` as their first parameter.

# Problem 11: Go back to a simple `Dog` class with `self.name = name` in the init.
# Below `__init__`, add a new method: `def bark(self):`. Inside it, print `"Woof!"`.
# Create `my_dog = Dog("Fido")` and call `my_dog.bark()`. 

# Problem 12: Because methods take `self`, they have access to the object's saved data!
# Add a method `def say_name(self):`. Inside it, print `self.name`. 
# Call `my_dog.say_name()`. 
# Expected Output: Fido

# Problem 13: Let's mutate (change) the data! 
# Inside your `Person` class, create a new method: `def yearPasses(self):`.
# Inside it, increment `self.age` by 1 (e.g., `self.age += 1`).

# Problem 14: Test the aging process. 
# Create `p = Person(10)`. 
# Call `p.yearPasses()` twice. 
# Print `p.age`. 
# Expected Output: 12

# Problem 15 (MINI-BOSS: AGE TIME MACHINE):
# Create `p = Person(-1)`. (This should trigger the HackerRank warning and set age to 0).
# Call `p.yearPasses()` once. 
# Print `p.age`. 
# Expected Output: 
# Age is not valid, setting age to 0.
# 1


# ==========================================
# SET 4: THE AM I OLD LOGIC (GRAND FINALE)
# ==========================================

# Problem 16: Outside of any class, let's just write the core logic. Set `age = 10`.
# Write an `if` statement: if age is less than 13, print `"You are young."`

# Problem 17: Add an `elif` statement. 
# In Python, you can chain comparisons! Write: `elif 13 <= age < 18:`
# Print `"You are a teenager."`

# Problem 18: Add an `else` statement. Print `"You are old."`

# Problem 19: Move this entire `if/elif/else` block into the `Person` class under a new method: `def amIOld(self):`.
# CAUTION: Inside the method, you can't just check `age`. You must check `self.age`!

# Problem 20 (THE GRAND FINALE):
# Assemble the final class! It should have:
# 1. `def __init__(self, initialAge):` with the validation logic.
# 2. `def amIOld(self):` with the printing logic.
# 3. `def yearPasses(self):` with the increment logic.
# Test it manually:
# p = Person(16)
# p.amIOld()
# p.yearPasses()
# p.yearPasses()
# p.amIOld()
# Expected Output: 
# You are a teenager.
# You are old.