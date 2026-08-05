# ==========================================
# PHASE 1: THE BLUEPRINT (NODES)
# ==========================================

# Problem 1: Class Definition
# Declare a class named `Node`.
class Node:

    # Problem 2: The Constructor
    # Write the initialization method (`__init__`) that accepts `self` and `data`.
    def __init__(self, data):
    
        # Problem 3: Storing the Data
        # Attach the passed-in `data` to the specific instance.
        self.data = data
        
        # Problem 4: The Chain (Pointer)
        # Create an attribute called `next`. This is the chain that will connect to the next train car.
        # Since this node was just created, it isn't connected to anything yet. Set it to `None`.
        self.next = None
        

# ==========================================
# PHASE 2: THE BUILDER (INSERT & DISPLAY)
# ==========================================

# Problem 5: The Manager Class
# Declare a new class called `Solution`.
class Solution:

    # Problem 6: The Insert Method
    # Define a method named `insert`. It needs to accept `self`, the `head` of the list, and the new `data`.
    def insert(self, head, data):
    
        # Problem 7: Building the Car
        # First things first, instantiate a new `Node` holding the `data` and save it to a variable called `p`.
        p = Node(data)
        
        # Problem 8: The Empty Train
        # Write an `if` statement to check if the train is completely empty (is the `head` equal to `None`?)
        if head == None:
        
            # Problem 9: If the train is empty, this new car `p` BECOMES the engine (`head`).
            # Assign `p` to `head`.
            head = p
            
        # Problem 10: Finding the Caboose
        # If the train is NOT empty (`else:`), we must attach the car to the very back.
        # But we only have the `head`! We need to walk to the end.
        else:
            
            # Problem 11: Create a temporary walking pointer named `current` and point it at the `head`.
            current = head
            
            # Problem 12: Write a `while` loop that runs as long as `current.next` is NOT `None`.
            # (Translation: "While there is a car attached behind me...")
            while current.next != None:
            
                # Problem 13: Inside the loop, move the pointer forward! 
                # Set `current` to equal `current.next`.
                current = current.next
                
            # Problem 14: Attaching the Car
            # Stepping out of the while loop, `current` is now officially the very last car (the caboose).
            # Set the `next` pointer of `current` to point to our new car `p`.
            current.next = p
            
        # Problem 15: Returning the Engine
        # At the very end of the method (outside the if/else), return the `head`.
        return head
    
    # ==========================================
    # PHASE 4: THE SWEEPER (REMOVE DUPLICATES)
    # ==========================================

    # Problem 17: The Method Definition
    # Inside the `Solution` class, define a method named `removeDuplicates`.
    # It must accept `self` and `head`.
    def removeDuplicates(self, head):
        # Problem 18: The Empty Train Check
        # If the train is completely empty, there is nothing to sweep!
        # Write an if statement: if the head is None, simply return the head.
        if head is None:
            return head

        # Problem 19: The Sweeper Pointer
        # Just like when we inserted a node, we need a walking pointer so we don't lose the head.
        # Create a variable called `current` and point it at the `head`.
        current = head

        # Problem 20: The Traversal Loop
        # We need to walk through the train, but we are going to be looking at the car AHEAD of us.
        # Write a while loop that continues as long as BOTH `current` is not None, 
        # AND `current.next` is not None.
        while current is not None and current.next is not None:
            # Problem 21: The Comparison
            # Inside the loop, check if the data in the car you are standing on (`current.data`) 
            # is EXACTLY EQUAL to the data in the car right in front of you (`current.next.data`).
            if current.data == current.next.data:
                # Problem 22: The Bypass (Deletion)
                # If they ARE equal, the car in front of you is a duplicate!
                # Do NOT move your `current` pointer forward. 
                # Instead, take your current chain (`current.next`) and hook it directly to 
                # the car TWO spaces ahead (`current.next.next`). 
                # You have just bypassed the duplicate!
                current.next = current.next.next
            # Problem 23: Moving Forward safely
            # Add an `else` block. If the car in front of you is NOT a duplicate, 
            # it is safe to walk forward. Move your `current` pointer to the next car.
            else:
                current = current.next
        # Problem 24: Return the Train
        # Outside of the while loop, return the `head` of the newly cleaned linked list.
        return head
        
    # Problem 16: The Display Method
    # Define a method named `display` that accepts `self` and `head`.
    def display(self, head):
        # I will give you this one to save time! We just walk the list and print.
        current = head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

# ==========================================
# PHASE 3: THE MATRIX (PARSING STDIN)
# ==========================================
# We are outside the Solution class now!

# Problem 25: The Setup
# Instantiate your `Solution` class to a variable named `mylist`.
# Read the first line of standard input, convert it to an integer, and save it to `T`.
# Create your empty `head` variable and set it to None.
mylist = Solution()
T = int(input())
head = None
# Problem 26: Building the List
# Create a for-loop that runs `T` times.
# Inside the loop, read the next integer from input and save it to `data`.
# Call the `insert` method on your manager, passing in the `head` and the `data`.
# CRITICAL: Just like the tree, capture the returned value and overwrite `head`!
for _ in range(T):
    data = int(input())
    head = mylist.insert(head, data)
# Problem 27: Sweeping the List
# The loop is finished, and the list is built!
# Call the `removeDuplicates` method on your manager, passing in the `head`.
# Overwrite your `head` variable with the cleaned list that gets returned!
head = mylist.removeDuplicates(head)
# Problem 28: The Final Display
# Call the `display` method on your manager, passing in the cleaned `head`.
mylist.display(head)