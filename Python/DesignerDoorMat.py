# ==========================================
# SET 1: THE INGREDIENTS
# ==========================================
# Let's set up the basic variables and inputs we need.
# NEW CONCEPT: HackerRank gives you inputs on one line like "9 27". 
# You can split them AND turn them into integers instantly using this magic line:
# N, M = map(int, input().split())

# Problem 1: Hardcode our test case for now. Set N = 9 and M = 27.
N = 9
M = 27
# Problem 2: Save the core pattern ".|." to a variable named `pattern`.
pattern = '.|.'

# Problem 3: Print `pattern` multiplied by 3. 
# Expected Output: .|..|..|.
print(pattern * 3)

# Problem 4: The middle belt is the easiest part. 
# Print the word "WELCOME" centered in a width of M, using "-" as the fill character.
# Expected Output: ----------WELCOME----------
print('WELCOME'.center(M, '-'))

# ==========================================
# SET 2: MASTERING THE CENTER METHOD
# ==========================================
# Let's see how our pattern interacts with the center method.

# Problem 5: Print `pattern` multiplied by 1, centered in a width of M, filled with "-".
# Expected Output: ------------.|.------------
print((pattern * 1).center(M, '-'))

# Problem 6: Print `pattern` multiplied by 3, centered in a width of M, filled with "-".
# Expected Output: ---------.|..|..|.---------
print((pattern * 3).center(M, '-'))

# Problem 7: Print `pattern` multiplied by 5, centered in a width of M, filled with "-".
# Expected Output: ------.|..|..|..|..|.------
print((pattern * 5).center(M, '-'))

# Problem 8: Look at the outputs from 5, 6, and 7. They exactly match the top of the door mat!
# What is the mathematical pattern of the multiplier? (Answer: It goes 1, 3, 5, 7... odd numbers!)
# odd numbers (% 2 != 0)

# ==========================================
# SET 3: THE ODD NUMBER GENERATOR
# ==========================================
# We need a `for` loop that skips even numbers and only gives us odd numbers.
# NEW CONCEPT: `range(start, stop, step)`
# If you add a third number to range, it tells Python how many steps to take.

# Problem 9: Write a `for` loop: `for i in range(1, 10, 2):` and print `i`.
# Expected Output: 
# 1
# 3
# 5
# 7
# 9
for i in range(1, 10, 2):
    print(i)

# Problem 10: Now let's combine it! For N = 9, the top half of the mat needs rows 1, 3, 5, 7.
# Write a `for` loop using `range(1, N, 2)`. 
# Inside, multiply `pattern` by `i`, and center it in width `M` filled with "-". Print it.
# Expected Output: (The entire top half of the door mat!)
N = 9
for i in range(1, N, 2):
    print((pattern * i).center(M, '-'))

# Problem 11: To build the bottom cone, we have to count BACKWARDS.
# Write a `for` loop: `for i in range(7, 0, -2):` and print `i`.
# Expected Output:
# 7
# 5
# 3
# 1
for i in range(7, 0, -2):
    print(i)

# Problem 12: Let's make that backwards range dynamic based on N. 
# If N = 9, the highest odd number below it is N - 2 (which is 7).
# Write a `for` loop using `range(N - 2, 0, -2)`. Print `i`.
# Expected Output: 7, 5, 3, 1
for i in range(N - 2, 0, -2):
    print((pattern * i).center(M, '-'))

# ==========================================
# SET 4: THE GRAND FINALE
# ==========================================
# You have built the top, the middle, and the bottom. Let's stack them!

# Problem 13: Let's use the magic input line so HackerRank can test different sizes.
# Copy this: N, M = map(int, input().split())
# (For testing in your IDE, when you run the code, type `9 27` into the console and hit Enter).

# Problem 14: Define your `pattern = ".|."`

# Problem 15: Create the TOP HALF. 
# Write a `for` loop from 1 up to N (stepping by 2). Print the centered pattern.

# Problem 16: Create the MIDDLE BELT.
# Print "WELCOME" centered in M. (No loop needed here, just one line!)

# Problem 17: Create the BOTTOM HALF.
# Write a `for` loop from N-2 down to 0 (stepping by -2). Print the centered pattern.

# Problem 18, 19, 20: Just bask in the glory of your finished code. You've solved it!