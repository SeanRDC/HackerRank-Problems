# ==========================================
# SET 1: THE BLUEPRINT (Python Classes)
# ==========================================

# MINI-LESSON: CLASSES AND THE CONSTRUCTOR
# To create a custom object, we define a `class`. 
# Every time a new object is created from this class, Python automatically runs a special setup function called the constructor: `def __init__(self):`
# The word `self` is incredibly important. It means "MY." If a robot wants to remember its own name, it doesn't save it to `name`, it saves it to `self.name`. 
def passable():
# Problem 1: Let's create our blueprint. 
# Define a class named `Solution`.
    class Solution:

    # Problem 2: Inside the class, write the constructor method. 
    # Write: `def __init__(self):`
        def __init__(self):

    # Problem 3: Inside the constructor, we need to give our object its own personal memory to hold the Stack.
    # Create an instance variable named `self.stack` and set it equal to an empty list `[]`.
            self.stack = []

    # Problem 4: Still inside the constructor, give our object a second memory bank for the Queue.
    # Create another instance variable named `self.queue` and set it equal to an empty list `[]`.
            self.queue = []

    # Problem 5 (MASTER PROBLEM 1: THE BLUEPRINT):
    # Review your code. You should have a `Solution` class, an `__init__` method, and two empty instance variables (`self.stack` and `self.queue`). 
    # (You can leave this set as is. No code execution needed yet).



    # ==========================================
    # SET 2: THE STACK (Last-In, First-Out)
    # ==========================================

    # MINI-LESSON: METHODS AND LIFO
    # A "Method" is just a function that lives inside a class. Because it lives inside the class, its first parameter MUST be `self` so it has access to the object's memory.
    # A Stack is LIFO (Last-In, First-Out). Think of a stack of plates. You add to the top, and you remove from the top. In a Python list, the "top" is just the very end of the list.

    # Problem 6: Define a new method inside your class (below `__init__`, same indentation level).
    # Name it `pushCharacter(self, ch)`. (The `ch` parameter represents the character we want to add).
        def pushCharacter(self, ch):

    # Problem 7: Inside this method, we need to add `ch` to the end of our stack. 
    # Use the `.append()` method on `self.stack` to add `ch`.
            self.stack.append(ch)

    # Problem 8: Now define the method to remove data. 
    # Name it `def popCharacter(self):` (No `ch` parameter needed, because we always just grab whatever is on top!)
        def popCharacter(self):

    # Problem 9: Inside this method, we need to remove and return the last item in the list.
    # Python lists have a built-in `.pop()` method that does exactly this. 
    # Write: `return self.stack.pop()`
            return self.stack.pop()

    # Problem 10: Concept Check (No code needed).
    # If we push 'A', then push 'B', our list is ['A', 'B']. When we call `popCharacter()`, it will look at the end of the list, remove 'B', and return it.


    # Problem 11: Let's test it in isolation! Outside your class (at the bottom of the file, un-indented):
    # 1. Instantiate the class: `test_obj = Solution()`
    # 2. Push two letters: `test_obj.pushCharacter('A')` then `test_obj.pushCharacter('B')`
    # 3. Print the popped letter: `print(test_obj.popCharacter())`
    # test_obj = Solution()
    # test_obj.pushCharacter('A')
    # test_obj.pushCharacter('B')
    # test_obj.popCharacter()
    # print(test_obj.display())

    # Problem 12 (MASTER PROBLEM 2: STACK ENGINE):
    # Run your code! If it prints 'B', your Stack is perfectly configured. 
    # (Once you verify it prints 'B', delete the dummy test code from Problem 11 so we can continue).



    # ==========================================
    # SET 3: THE QUEUE (First-In, First-Out)
    # ==========================================

    # MINI-LESSON: FIFO AND REMOVING FROM THE FRONT
    # A Queue is FIFO (First-In, First-Out). Think of a line at a grocery store. 
    # When people join the line, they go to the BACK (just like a stack). But when the cashier serves someone, they take the person at the very FRONT of the line (index 0).

    # Problem 13: Define a new method inside your class named `enqueueCharacter(self, ch)`.
        def enqueueCharacter(self, ch):

    # Problem 14: Inside this method, add `ch` to the back of our queue. 
    # Use `.append()` on `self.queue` to add `ch`. (Notice this is identical to push!)
            self.queue.append(ch)

    # Problem 15: Define the method to serve the data. 
    # Name it `def dequeueCharacter(self):`
        def dequeueCharacter(self):

    # Problem 16: Inside this method, we need to remove and return the FIRST item in the list.
    # If `.pop()` removes the last item, how do we remove the first? By passing the index!
    # Write: `return self.queue.pop(0)`
            return self.queue.pop(0)

    # Problem 17: Concept Check (No code needed).
    # If we enqueue 'A', then enqueue 'B', our list is ['A', 'B']. When we call `dequeueCharacter()`, it looks at index 0, removes 'A', and returns it. 


    # Problem 18: Let's test it in isolation! Outside your class:
    # 1. Instantiate: `test_obj = Solution()`
    # 2. Enqueue two letters: `test_obj.enqueueCharacter('A')` then `test_obj.enqueueCharacter('B')`
    # 3. Print the dequeued letter: `print(test_obj.dequeueCharacter())`
    # test_obj = Solution()
    # test_obj.enqueueCharacter('A')
    # test_obj.enqueueCharacter('B')
    # print(test_obj.dequeueCharacter())

    # Problem 19 (MASTER PROBLEM 3: QUEUE ENGINE):
    # Run your code! If it prints 'A', your Queue is perfectly configured.
    # (Once you verify it prints 'A', delete the dummy test code from Problem 18).



    # ==========================================
    # SET 4: THE DRIVER CODE (Loading Phase)
    # ==========================================

    # MINI-LESSON: ASSEMBLING THE CONTAINERS
    # Our blueprint is complete. Now we write the "Driver Code" (the main program) to actually use our custom object to solve the Palindrome problem.

    # Problem 20: Outside the class, read standard input into a variable named `s`.
    s = input()

    # Problem 21: Create a real instance of your `Solution` class and assign it to a variable named `obj`.
    obj = Solution()

    # Problem 22: Get the length of the string `s` and store it in a variable named `l`.
    l = len(s)

    # Problem 23: Write a standard `for` loop that iterates `l` times, using `i` as the loop variable.
    for i in range(l):

    # Problem 24 (MASTER PROBLEM 4: DUAL LOADING):
    # Inside the loop, extract the current character from the string `s` using the index `i`.
    # Feed that character into your stack: `obj.pushCharacter(s[i])`
    # Feed that same character into your queue: `obj.enqueueCharacter(s[i])`
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    # ==========================================
    # SET 5: THE PALINDROME SHOWDOWN
    # ==========================================

    # MINI-LESSON: THE COLLISION
    # If the word is "racecar", the Stack will spit it out backwards, and the Queue will spit it out forwards. If they match every single time, it's a palindrome!

    # Problem 25: Create a boolean flag named `isPalindrome` and set it to `True`.
    isPalindrome = True

    # Problem 26: We only need to check half the word because the ends are meeting in the middle!
    # Write a `for` loop that iterates exactly half the length of the word: `for i in range(l // 2):`
    for i in range(1 // 2):

    # Problem 27: Inside this loop, it's time for the showdown. 
    # Write an `if` statement that calls your pop method and your dequeue method, and checks if they do NOT equal each other (!=).
    # Hint: `if obj.popCharacter() != obj.dequeueCharacter():`
        if obj.popCharacter() != obj.dequeueCharacter():

    # Problem 28: If they do NOT match, the word is busted. 
    # Inside the `if` block, change `isPalindrome` to `False` and immediately `break` out of the loop.
            isPalindrome = False
            break

    # Problem 29: Outside the loop, write a final `if/else` block that looks at `isPalindrome`.
    # If true, print exactly: "The word, " + s + ", is a palindrome."
    # If false, print exactly: "The word, " + s + ", is not a palindrome."
    if isPalindrome == True:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")
pass
# Problem 30 (THE GRAND FINALE):
# Assemble everything! Your Class definitions, your instance variables, your LIFO/FIFO methods, and your driver code logic!


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.pop(0)
    
s = input()
l = len(s)
obj = Solution()

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome == False:
    print(f"The word, {s}, is not a palindrome.")
else:
    print(f"The word, {s}, is a palindrome.")