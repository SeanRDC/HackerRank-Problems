# ==========================================
# SET 1: THE BLUEPRINT & ENCAPSULATION
# ==========================================

# MINI-LESSON: SCOPE AND PRIVATE VARIABLES
# In Python, sometimes we want to protect our data so outside code can't accidentally change it.
# We do this by putting two underscores (`__`) in front of a variable name. 
# This is called "Encapsulation". It makes the variable PRIVATE. It can only be seen inside the class!

# Problem 1: Define a class named `Difference`. 
# Put `pass` inside it for now.
class Difference:

# Problem 2: Delete `pass`. Define the constructor method `__init__`.
# It needs to take two things: `self` and `a` (which will be our array of numbers).
    def __init__(self, a):

# Problem 3: Inside the constructor, we want to save `a` as a PRIVATE instance variable. 
# Save `a` into `self.__elements`. (Those two underscores are the magic shield!)
        self.__elements = a

# Problem 4: The problem requires us to store our final answer in a PUBLIC variable.
# Still inside the constructor, create `self.maximumDifference` and initialize it to `0`.
        self.maximumDifference = 0


# Problem 5 (MINI-BOSS: THE BUILDER):
# Review your constructor. It should take `a`, save it to the private `__elements`, 
# and set up the public `maximumDifference` to 0. Send Set 1 over for review!

# ==========================================
# SET 2: THE CORE LOGIC (Math & Built-ins)
# ==========================================

# MINI-LESSON: BUILT-IN EFFICIENCY
# Instead of comparing every single pair of numbers (which takes forever), we just need to find the absolute maximum and minimum numbers in the list and subtract them!

# Problem 6: Inside the class, below the constructor, define a new instance method:
# `def computeDifference(self):`
    def computeDifference(self):

# Problem 7: Inside this method, we need the smallest number in our private array.
# Create a variable called `min_val`. Use Python's built-in `min()` function on `self.__elements`.
        min_val = min(self.__elements)

# Problem 8: Now we need the biggest number. 
# Create a variable called `max_val`. Use Python's built-in `max()` function on `self.__elements`.
        max_val = max(self.__elements)

# Problem 9: Calculate the absolute difference. Since `max_val` is always greater than or equal to `min_val`, we can just subtract them!
# Create a variable called `diff` and set it to `max_val - min_val`.
# (Alternatively, you can wrap it in Python's `abs()` function just to be extra safe: `abs(max_val - min_val)`).
        diff = abs(max_val - min_val)

# Problem 10 (MINI-BOSS: SAVING THE STATE):
# We need to save this answer so the outside world can see it. 
# Overwrite your `self.maximumDifference` instance variable with the `diff` you just calculated.
        self.maximumDifference = diff


# ==========================================
# SET 3: LIST COMPREHENSIONS (The Precode)
# ==========================================

# MINI-LESSON: LIST COMPREHENSIONS & THROW-AWAY VARIABLES
# HackerRank uses a really cool Python trick here to build the array from user input on a single line!

# Problem 11: Outside the class, at the bottom of the script, write the execution block:
# `if __name__ == '__main__':`


# Problem 12: The first line of input is the size of the array. But Python lists can grow dynamically, so we don't actually need to know the size!
# In Python, if we have to take an input but don't care about saving it, we use an underscore `_` as a "throw-away" variable.
# Inside the `if` block, write: `_ = input()`
if __name__ == '__main__':

# Problem 13: The next line of input is a string of numbers separated by spaces (e.g., "1 2 5").
# Write `input().split(' ')` to get a list of string numbers, but don't assign it to anything just yet.

# Problem 14: HackerRank uses a "list comprehension" to turn those strings into integers instantly.
# Create a variable `a` and set it to: `[int(e) for e in input().split(' ')]`
# (This literally reads: "Make a list of integer versions of 'e', for every 'e' inside our split string").
    a = [int(e) for e in input().split()]

# Problem 15 (MINI-BOSS: THE INPUT HANDLER):
# Review your driver code. It should be taking the throwaway size, and properly parsing the array of numbers into `a`.
    print(a)


# ==========================================
# SET 4: EXECUTION & GRAND FINALE
# ==========================================

# MINI-LESSON: SCOPE IN ACTION
# Now we use our class. Because `maximumDifference` is public, we can print it down here. If we tried to print `__elements`, Python would throw a strict security error!

# Problem 16: Still inside the `if __name__` block, instantiate your class!
# Create a variable `d` and set it equal to `Difference(a)`.
    d = Difference(a)

# Problem 17: Tell your object to do the math. 
# Call the method `d.computeDifference()`.
    d.computeDifference()

# Problem 18: The object has calculated the difference and stored it internally. 
# Print the public variable by writing: `print(d.maximumDifference)`
    print(d.maximumDifference)

# Problem 19 (CONCEPT CHECK - No code needed): 
# Realize what just happened. The driver code gave the data to the object, asked it to do the work, and then asked for the final answer. The driver code didn't do any of the math itself! This is the beauty of Object-Oriented Programming.


# Problem 20 (THE GRAND FINALE):
# Assemble your full script! The encapsulated class, the min/max math logic, and the driver code.


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================