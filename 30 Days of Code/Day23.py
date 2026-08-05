# ==========================================
# PHASE 1: THE BLUEPRINT (NODES)
# ==========================================

# CONCEPT: WHAT IS A TREE?
# Imagine a physical family tree. It is made up of individuals. 
# In Computer Science, we call these individuals "Nodes". 
# Before we can build a tree, we have to teach the computer what a single "Node" is.
# A Node needs three things:
# 1. A piece of data (the value it holds, like the number 5).
# 2. A pointer to a left child.
# 3. A pointer to a right child.

# Problem 1: Class Definition
# We need to create a blueprint for our nodes. 
# Declare a class and name it appropriately (capitalized by convention).
class Node:

    # Problem 2: The Constructor
    # Every time a new node is created, it needs to be set up immediately.
    # Write the special Python initialization method (the constructor). 
    # It must accept the instance itself, as well as a parameter for the data it will hold.
    def __init__(self, data):
    
        # Problem 3: Storing the Data
        # Inside the constructor, take the data that was passed in and attach it securely 
        # to the specific instance of the object being created.
        self.data = data
        
        # Problem 4: Initializing the Pointers
        # When a node is first born, it has no children. It is completely alone.
        # Create two attributes for the instance: one for the left child, and one for the right.
        # Set both of them to represent absolute "emptiness" or "nothing" in Python.
        self.left = None
        self.right = None
        
# ==========================================
# TEST YOUR CODE
# ==========================================
# If you did this correctly, you should be able to run this test code below without errors!
# (Uncomment the lines below to test)

my_first_node = Node(42)
print(f"My node holds the value: {my_first_node.data}")
print(f"Left child is: {my_first_node.left}")
print(f"Right child is: {my_first_node.right}")