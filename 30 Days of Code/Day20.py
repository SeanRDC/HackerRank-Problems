# ==========================================
# SET 1: THE MECHANICS OF A SWAP
# ==========================================

# 1. Here is our sample input (Test Case)
a = [5, 3]

# Problem 5: Create your total_swaps variable and set it to 0.
total_swaps = 0

# Problem 2: Write an `if` statement to check if the element at index 0 is greater than index 1.
if a[0] > a[1]:

    # Problem 3: Inside the `if`, use the Pythonic trick to swap a[0] and a[1].
    a[0], a[1] = a[1], a[0]
    
    # Problem 6: Still inside the `if`, increment total_swaps by 1.
    total_swaps += 1


# ==========================================
# TEST CASE VERIFICATION
# ==========================================
print(f"Array after swap: {a}")
print(f"Total swaps: {total_swaps}")

# EXPECTED OUTPUT: 
# Array after swap: [3, 5]
# Total swaps: 1

# ==========================================
# SET 2: THE INNER LOOP (One Full Pass)
# ==========================================

# MINI-LESSON: AVOIDING THE "INDEX OUT OF BOUNDS" ERROR
# We need to do this swap check for the entire array. We will use a loop variable `j` to represent our current index.
# We will compare `a[j]` and `a[j + 1]`. 

# 1. Here is our new sample input for this phase
a = [4, 3, 2, 1]
n = len(a)
total_swaps = 0

# Problem 8: Because we are always looking one step ahead (`j + 1`), our loop must stop one step EARLY.
# Write a `for` loop using `j` that iterates up to `n - 1`. 
# (Hint: use range())
for j in range(n - 1):

    # Problem 9: Inside this loop, write the `if` statement checking if `a[j]` is greater than `a[j + 1]`.
    if a[j] > a[j + 1]:
    
        # Problem 10: Inside the `if` block, perform the Pythonic swap on `a[j]` and `a[j + 1]`.
        a[j], a[j + 1] = a[j + 1], a[j]
        
        # Problem 11: Still inside the `if` block, increment `total_swaps` by 1.
        total_swaps += 1


# ==========================================
# TEST CASE VERIFICATION
# ==========================================
print(f"Array after one pass: {a}")
print(f"Total swaps so far: {total_swaps}")

# EXPECTED OUTPUT: 
# Array after one pass: [3, 2, 1, 4]
# Total swaps so far: 3

# ==========================================
# SET 3: THE OUTER LOOP (Repeating the Process)
# ==========================================

# 1. Here is our test case again. Notice total_swaps starts at 0 OUTSIDE the loops.
a = [4, 3, 2, 1]
n = len(a)
total_swaps = 0

# Problem 13: Write an outer `for` loop using `i` that iterates `n` times. (Use range(n))
for i in range(n):

    # Problem 17: We need a way to track if we did any swaps during THIS SPECIFIC pass. 
    # Inside the outer loop, create a variable named `current_swaps` and set it to 0.
    current_swaps = 0
    
    # Problem 14: Place your entire inner `for` loop (the one using `j`) inside this new outer loop.
    # (Copy your perfect code from Set 2 here, making sure it is indented properly)
    for j in range(n - 1):
        # (Inside your j loop...)
        if a[j] > a[j + 1]:
            # (Inside your if statement...)
            a[j], a[j + 1] = a[j + 1], a[j]
            # (Swap the elements)
            total_swaps += 1
            # (Increment total_swaps)
            
            # Problem 19 (Prep for optimization): Also increment `current_swaps` by 1 right here!
            current_swaps += 1 

# ==========================================
# TEST CASE VERIFICATION
# ==========================================
print(f"Array after full sort: {a}")
print(f"Total swaps to sort: {total_swaps}")

# EXPECTED OUTPUT: 
# Array after full sort: [1, 2, 3, 4]
# Total swaps to sort: 6

# ==========================================
# SET 4: THE OPTIMIZATION (Early Exit)
# ==========================================

# 1. Here is our test case. We'll use a mostly-sorted array to prove the early exit works!
a = [1, 2, 4, 3]
n = len(a)
total_swaps = 0

for i in range(n):
    current_swaps = 0
    
    # Inner loop
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            total_swaps += 1
            current_swaps += 1
            
    # Problem 20: Step OUT of the inner loop, but stay INSIDE the outer loop.
    # (Your indentation should match the `for j...` line)
    # Write an `if` statement checking if `current_swaps` is equal to 0.
    if current_swaps == 0:
    
        # Problem 21: If it is 0, it means no items were out of order.
        # Inside this `if` block, write the `break` command to instantly kill the outer loop.
        break


# ==========================================
# TEST CASE VERIFICATION
# ==========================================
print(f"Array after optimized sort: {a}")
print(f"Total swaps to sort: {total_swaps}")

# EXPECTED OUTPUT: 
# Array after optimized sort: [1, 2, 3, 4]
# Total swaps to sort: 1

# ==========================================
# SET 5: THE OUTPUT & ASSEMBLY
# ==========================================

# Problem 30 (GRAND FINALE): Assemble the entire script!

# 1. Here is HackerRank's required pre-code to read the input (Do not change this):
import sys
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # 2. Paste your variable initialization (total_swaps = 0) here.
    total_swaps = 0
    
    # 3. Paste your perfectly optimized double-loop here.
    for i in range(n):
        current_swaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                total_swaps += 1
                current_swaps += 1
        if current_swaps == 0:
            break
    
    # 4. We are out of the loops! Time to print the results.
    # Problem 27: Print the total swaps string. (Hint: Use an f-string)
    # Target output format: Array is sorted in X swaps.
    print(f"Array is sorted in {total_swaps} swaps.")
    
    # Problem 28: Print the first element string.
    # Target output format: First Element: Y
    print(f"First Element: {a[0]}")
    
    # Problem 29: Print the last element string.
    # Target output format: Last Element: Z
    print(f"Last Element: {a[-1]}")

# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================