# ==========================================
# SET 1: THE BLUEPRINT & THE STACK (LIFO)
# ==========================================

# Problem 1: We need an object to hold our data structures. 
# Define a class named `Solution`. Inside it, write the standard constructor method that initializes an object when it is created.


# Problem 2: Inside the constructor, we need our two containers. 
# Create an instance variable for your stack and initialize it as an empty list. 
# Create a second instance variable for your queue and initialize it as an empty list as well.


# Problem 3: A Stack operates on a Last-In, First-Out (LIFO) basis. 
# Define a method `pushCharacter(self, ch)` that takes a character. How do you add an item to the very top (the end) of a standard Python list? Write the logic inside this method.


# Problem 4: Now we need to retrieve data from the stack.
# Define a method `popCharacter(self)`. It needs to remove the plate at the very top of the stack (the last item) and hand it back to us. 
# Write the logic to remove and return the last item in your stack list.


# Problem 5 (MASTER PROBLEM 1: THE STACK ENGINE):
# Assemble the `Solution` class, the constructor, and your two stack-related methods. 
# Ensure your logic correctly adds items to the end and removes them from the end.



# ==========================================
# SET 2: THE QUEUE (FIFO)
# ==========================================

# Problem 6: A Queue operates on a First-In, First-Out (FIFO) basis. 
# Define a method `enqueueCharacter(self, ch)`. When a person gets in a line, where do they go? They go to the back! 
# Write the logic to add the character to the back (the end) of your queue list.


# Problem 7: Now we need to serve the people in the queue. 
# Define a method `dequeueCharacter(self)`. Who gets served first? The person at the very front of the line!
# Write the logic to remove and return the item at the exact beginning (index 0) of your queue list.


# Problem 8: Concept Check (No code needed).
# Notice that `push` and `enqueue` do the exact same thing (add to the end of the list). The magic difference between a Stack and a Queue only happens when we *remove* data!


# Problem 9: Concept Check (No code needed).
# If we push the letters "C", "A", "T" to our stack, and enqueue "C", "A", "T" to our queue, what letter will `popCharacter` return? What letter will `dequeueCharacter` return? 
# (Answer: Stack pops 'T'. Queue dequeues 'C').


# Problem 10 (MASTER PROBLEM 2: THE FULL CLASS):
# Add the two queue methods to your `Solution` class. 
# Your class is now a fully functional dual-data-structure engine! 



# ==========================================
# SET 3: THE DRIVER CODE (Data Loading)
# ==========================================

# Problem 11: We need to get the user's word. 
# Outside and below your class (no indentation), read standard input into a variable named `s`.


# Problem 12: We need to hire a manager to run our containers. 
# Instantiate a new object of your `Solution` class and assign it to a variable named `obj`.


# Problem 13: We need to know how many letters are in the word so we can process them.
# Get the length of the string `s` and store it in a variable named `l`.


# Problem 14: We need to look at every single letter in the word one by one. 
# Write a standard `for` loop that iterates `l` times, using `i` as the loop variable.


# Problem 15 (MASTER PROBLEM 3: LOADING THE CONTAINERS):
# Inside your loop, grab the current character from the string `s` using the index `i`.
# Feed that character into your stack using your `pushCharacter` method.
# On the next line, feed that same character into your queue using your `enqueueCharacter` method.



# ==========================================
# SET 4: THE PALINDROME SHOWDOWN
# ==========================================

# Problem 16: The containers are loaded. Now we evaluate. 
# Create a boolean flag named `isPalindrome` and set its initial value to `True` (assume innocent until proven guilty).


# Problem 17: We only need to check half the word because the ends are meeting in the middle!
# Write a `for` loop that iterates exactly half the length of the word (use integer division).


# Problem 18: Inside this loop, it is time for the showdown. 
# Write an `if` statement that checks: Does the next letter popped from the stack NOT equal the next letter dequeued from the queue?


# Problem 19: If they do NOT match, the word is dead. 
# Inside the `if` block, change `isPalindrome` to `False` and immediately break out of the loop.


# Problem 20 (GRAND FINALE: THE VERDICT):
# Outside the loop, write a final `if/else` block that looks at `isPalindrome`.
# If true, print exactly: "The word, [word], is a palindrome."
# If false, print exactly: "The word, [word], is not a palindrome."
# (Hint: Use string concatenation (+) or an f-string to inject the variable `s`).


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================