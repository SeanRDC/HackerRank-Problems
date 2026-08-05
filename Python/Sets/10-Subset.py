# ==========================================
# PHASE 1: THE TEST CASE LOOP
# ==========================================

# Problem 1: The Number of Tests
# Read the very first line of standard input, convert it to an integer, and save it to `T`.
T = int(input())

# Problem 2: The Master Loop
# Create a for-loop that runs `T` times. Everything else we write will go INSIDE this loop.
for i in range(T):


    # ==========================================
    # PHASE 2: PARSING SET A AND SET B
    # ==========================================

    # Problem 3: The Size of A (The Throwaway)
    # Read the next line of input using `input()`. We don't care about this number, 
    # so assign it to a "dummy" variable named `_` (just an underscore).
    _ = input()
    
    # Problem 4: Building Set A
    # Read the next line, split it by spaces, turn it into a list, and convert it to a set.
    # (Hint: use set(input().split()) )
    # Save this to a variable named `A`.
    A = set(input().split())
    
    # Problem 5: The Size of B (The Throwaway)
    # Read the next line using `input()` and assign it to `_` again to throw it away.
    _ = input()
    
    
    # Problem 6: Building Set B
    # Read the next line, split it, convert it to a set, and save it to `B`.
    B = set(input().split())
    
    # ==========================================
    # PHASE 3: THE SUBSET CHECK
    # ==========================================

    # Problem 7: The Magic Method
    # Still inside the loop! Use Python's built-in `.issubset()` method to check 
    # if A is a subset of B. 
    # Wrap that method call directly inside a `print()` function so it prints True or False!
    print(A.issubset(B))