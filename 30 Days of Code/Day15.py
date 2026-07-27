# ==========================================
# SET 1: THE NODE & THE SOLUTION SHELL
# ==========================================

# MINI-LESSON: NODES AND POINTERS
# A Linked List is made up of `Node` objects. 
# Every Node needs two things: `data` (the actual value) and `next` (a pointer to the next Node).
# If `next` is `None`, it means we are at the very end of the train!

# Problem 1: Define a class named `Node`. Define its constructor `__init__(self, data):`


# Problem 2: Inside the constructor, save the data: `self.data = data`.
# On the next line, initialize the pointer to nothing: `self.next = None`.
# (Every new node starts off unattached to anything).


# Problem 3: Below the Node class, define a new class named `Solution`.
# (This is just a wrapper class HackerRank uses to hold our methods).
# Inside it, define a method to print the list: `def display(self, head):`


# Problem 4: Inside `display`, we create a temporary pointer so we don't lose the head: `current = head`.
# Write a `while current:` loop. Inside the loop, print the data: `print(current.data, end=' ')`.
# Then, move the pointer to the next node: `current = current.next`.
# (This is exactly how you "walk" through a train!)


# Problem 5 (MINI-BOSS: THE SHELLS ARE READY):
# Your `Node` class and `display` method are done. 
# Below `display`, define the method we actually need to solve: `def insert(self, head, data):`
# Just put `pass` inside it for now, and send Set 1 over for review!



# ==========================================
# SET 2: THE INSERTION (BASE CASE)
# ==========================================

# MINI-LESSON: THE HEAD AND THE EDGE CASE
# The `head` is the very first Node in the list. If `head` is `None`, it means the train has no cars at all!
# The absolute first step of insertion is creating the new car. 

# Problem 6: Delete `pass` in your `insert` method. 
# Create a new Node using the data passed in. 
# Write: `new_node = Node(data)`


# Problem 7: Now we must handle the edge case. Is the list completely empty?
# Write an `if` statement to check if `head` is `None`.


# Problem 8: If `head` is `None`, this new node is the very first car. 
# Inside the `if` block, assign `head` to equal `new_node`.


# Problem 9: The method expects us to return the starting point of the list.
# Still inside the `if` block, `return head`.


# Problem 10 (MINI-BOSS: EMPTY LIST HANDLED):
# Review your `insert` method. It should create the node, check if the head is None, 
# set the head to the new node if it is, and return it. 



# ==========================================
# SET 3: TRAVERSING TO THE TAIL
# ==========================================

# MINI-LESSON: WALKING THE TRAIN
# If `head` is NOT None, the list already has cars. We must find the last car (the tail) so we can attach our `new_node` to it.
# We CANNOT change `head` itself, otherwise we lose the front of our train! We must use a temporary "walker" variable.

# Problem 11: Below your `if` block, write an `else:` statement. 


# Problem 12: Inside the `else` block, create a temporary pointer named `current` and set it equal to `head`.
# (We will use `current` to walk down the train).


# Problem 13: We need to walk forward UNTIL the current car's chain (`current.next`) is empty (`None`).
# Write a while loop: `while current.next is not None:`


# Problem 14: Inside the while loop, we simply take one step forward.
# Write: `current = current.next`
# (When this loop finally breaks, `current` will be standing on the very last node!)


# Problem 15 (MINI-BOSS: ATTACH AND RETURN):
# OUTSIDE the while loop (but still inside the `else` block), `current` is now the tail node.
# Hook up the new car! Set `current.next` equal to `new_node`.
# Finally, at the very bottom of the entire method, `return head`.



# ==========================================
# SET 4: THE DRIVER CODE & GRAND FINALE
# ==========================================

# MINI-LESSON: HOW HACKERRANK TESTS IT
# We need to read `T` (the number of test cases) and build the list one by one.

# Problem 16: At the bottom of the script (no indentation), instantiate the `Solution` class:
# `mylist = Solution()`
# Then read `T = int(input())` and set `head = None`.


# Problem 17: Create a `for` loop that runs `T` times: `for i in range(T):`
# Inside it, read the data: `data = int(input())`.


# Problem 18: We need to insert this data and update our head. 
# Inside the loop, call your method: `head = mylist.insert(head, data)`
# (Notice how we overwrite `head`? This is why we had to `return head` at the end of our method!)


# Problem 19: Outside the `for` loop, print the entire finished list.
# Call: `mylist.display(head)`


# Problem 20 (THE GRAND FINALE):
# Assemble your full script! The `Node` class, the `Solution` class with `display` and `insert`, and the driver code!


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================