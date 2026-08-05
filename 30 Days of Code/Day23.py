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

# ==========================================
# PHASE 2: THE ARCHITECT (RECURSIVE INSERTION)
# ==========================================

# Problem 5: The Manager Class
# Declare a new class called `Solution`. This will hold our tree-building methods.


    # Problem 6: The Insert Method
    # Define a method named `insert`. It needs to accept three things:
    # 1. The instance itself.
    # 2. A pointer to the current `root` node we are looking at.
    # 3. The `data` we want to add to the tree.
    
    
        # CONCEPT: THE BASE CASE
        # A recursive function must know when to stop. 
        # In a tree, we stop when we hit an empty space. This is where the new leaf grows!
        
        # Problem 7: The Empty Spot
        # Write a condition to check if the current `root` represents "nothing".
        # If it does, instantiate a brand new `Node` holding the `data`, and return it.
        
        
        # CONCEPT: NAVIGATING THE TREE
        # If the spot is NOT empty, we must decide whether to go left or right.
        else:
            # Problem 8: The Left Path
            # Write a condition to check if the `data` is less than or equal to the current root's data.
            
            
                # Problem 9: Recursive Attachment (Left)
                # If it's smaller, we ask the left child to handle the insertion.
                # Call this `insert` method again, passing it the left child and the data.
                # CRITICAL: You must catch the result of this call and assign it to the current root's left pointer!
                # This "stitches" the tree together.
                
                
            # Problem 10: The Right Path
            # Write the alternative condition for when the `data` is strictly greater.
            
            
                # Problem 11: Recursive Attachment (Right)
                # Do the exact same thing as Problem 9, but for the right child.
                # Recursively call insert on the right child and attach the result to the right pointer.
                
                
        # Problem 12: Stitching it all together
        # At the very end of the method (outside the if/else routing, but inside the method), 
        # return the current `root`. This hands the updated branch back up to the parent!
        
        

# ==========================================
# TEST YOUR CODE
# ==========================================
# Uncomment the code below to test your architect!

# myTree = Solution()
# root = None
# root = myTree.insert(root, 3)
# root = myTree.insert(root, 1)
# root = myTree.insert(root, 4)

# print(f"Root: {root.data}")
# print(f"Left Child: {root.left.data}")
# print(f"Right Child: {root.right.data}")