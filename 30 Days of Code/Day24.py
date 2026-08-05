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
        
    # Problem 16: The Display Method
    # Define a method named `display` that accepts `self` and `head`.
    def display(self, head):
        # I will give you this one to save time! We just walk the list and print.
        current = head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

# ==========================================
# TEST YOUR CODE
# ==========================================
myList = Solution()
head = None

# Adding cars to the train
head = myList.insert(head, 1)
head = myList.insert(head, 2)
head = myList.insert(head, 2)
head = myList.insert(head, 3)
head = myList.insert(head, 4)

# Printing the train
myList.display(head) 