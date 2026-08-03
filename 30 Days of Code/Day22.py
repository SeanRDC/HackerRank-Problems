# ==========================================
# SET 1: RECURSION AND THE BINARY TREE
# ==========================================

# MINI-LESSON: TREES AND RECURSION
# A Binary Tree is made of "Nodes". Each node has data, and points to a left child (root.left) and a right child (root.right).
# To find the total height, a node asks its children for their height. 
# Those children ask THEIR children, and so on, until they hit an empty spot (None).

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    # (HackerRank's provided insert function is hidden here for our testing purposes)
    
    def getHeight(self,root):
        # Problem 1: The Base Case (When to stop digging)
        # If a node doesn't exist, we've hit the absolute bottom.
        # Write an `if` statement to check if `root` is equal to `None`.
        if root == None:
        
            # Problem 2: If it is None, return -1. 
            # (Why -1? Because the height is the number of EDGES. A single leaf node has 0 edges. 
            # By returning -1 for an empty space, the math (-1 + 1) perfectly equals 0 for a leaf!)
            return -1
            
        # Problem 3: The Recursive Step (Digging down the left)
        # Create a variable named `left_height`. 
        # Set it equal to `self.getHeight(...)`, passing in the left child (`root.left`).
        # Yes, you are calling the exact same function you are currently writing!
        left_height = self.getHeight(root.left)
        
        # Problem 4: The Recursive Step (Digging down the right)
        # Create a variable named `right_height`.
        # Set it equal to `self.getHeight(...)`, passing in the right child (`root.right`).
        right_height = self.getHeight(root.right)
        
        # Problem 5 (MASTER PROBLEM): 
        # We want the longest path. Find the maximum of `left_height` and `right_height` using Python's built-in `max(a, b)` function.
        # Add 1 to that maximum (to count the edge connecting to the current node), and `return` the result!
        return max(left_height, right_height) + 1

# ==========================================
# TEST CASE VERIFICATION
# ==========================================
# We will manually build the exact tree from the HackerRank sample:
#      3
#    /   \
#   2     5
#  /     / \
# 1     4   6
#            \
#             7
# The longest path is 3 -> 5 -> 6 -> 7 (which is exactly 3 edges).

myTree = Solution()
test_root = Node(3)
test_root.left = Node(2)
test_root.left.left = Node(1)
test_root.right = Node(5)
test_root.right.left = Node(4)
test_root.right.right = Node(6)
test_root.right.right.right = Node(7)

print(f"Height of the tree: {myTree.getHeight(test_root)}")

# EXPECTED OUTPUT: 
# Height of the tree: 3