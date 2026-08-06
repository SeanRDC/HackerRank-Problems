# ==========================================
# PHASE 1: THE SETUP
# ==========================================

# Problem 1: The Sizes
# Read the first line using input(). We don't actually need to use these numbers, 
# but we must read the line so we can move on to the actual data.
_ = input().split()

# Problem 2: The Array
# Read the second line, split it, and save it as a `list` named `array`. 
# CRITICAL: Do not convert this to a set! We need to process every single duplicate.
array = list(input().split())

# Problem 3: Set A (Things we like)
# Read the third line, split it, and save it as a `set` named `A`.
A = set(input().split())

# Problem 4: Set B (Things we dislike)
# Read the fourth line, split it, and save it as a `set` named `B`.
B = set(input().split())

# ==========================================
# PHASE 2: CALCULATING HAPPINESS
# ==========================================

# Problem 5: The Score
# Initialize a variable named `happiness` and set it to 0.
happiness = 0

# Problem 6: The Loop
# Write a for-loop that goes through every `item` in your `array`.
for item in array:

    # Problem 7: The Good
    # Inside the loop, check if the `item` is in set `A`. If it is, add 1 to `happiness`.
    if item in A:
        happiness += 1
    
    # Problem 8: The Bad
    # Check if the `item` is in set `B`. If it is, subtract 1 from `happiness`.
    elif item in B:
        happiness -= 1

# ==========================================
# PHASE 3: THE OUTPUT
# ==========================================

# Problem 9: The Result
# Step completely outside the loop and print your final `happiness`.
# Mock input:
# 3 2
# 1 5 3
# 3 1
# 5 7
print(happiness)