# ==========================================
# PHASE 1: THE SETUP
# ==========================================

# Problem 1: Set A
# Read the first line, split it, and convert it directly into a set named `A`.
A = set(input().split())

# Problem 2: Number of other sets
# Read the second line and convert it to an integer named `N`.
N = int(input())

# ==========================================
# PHASE 2: THE BOOLEAN FLAG
# ==========================================

# Problem 3: The Flag
# Create a variable named `is_strict` and set it to True. 
# We assume A is a strict superset of everything until proven otherwise!
is_strict = True

# ==========================================
# PHASE 3: THE VERIFICATION LOOP
# ==========================================

# Problem 4: The Loop
# Create a loop that runs `N` times.
for _ in range(N):

    # Problem 5: Set B
    # Inside the loop, read the next line and convert it into a set named `B`.
    B = set(input().split())
    
    # Problem 6: The Strict Superset Check
    # Write an `if` statement to check if A is NOT a strict superset of B.
    # (Hint: if not (A > B): )
    if not (A > B):
        
        # Problem 7: Flipping the Flag
        # If it fails, set your `is_strict` flag to False.
        is_strict = False
        
        # Problem 8: The Early Exit
        # Since it only takes one failure to ruin the entire test, 
        # use `break` to exit the loop immediately and save processing time.
        break
        
# ==========================================
# PHASE 4: THE VERDICT
# ==========================================

# Problem 9: The Output
# Completely outside the loop, print the final value of your `is_strict` flag.
print(is_strict)