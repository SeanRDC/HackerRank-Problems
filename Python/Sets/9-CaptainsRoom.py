# ==========================================
# PHASE 1: THE REGISTRY (DICTIONARIES)
# ==========================================

# Problem 1: The Setup
# Create a variable called `room_counts` and assign it to an empty dictionary. 
# (In Python, an empty dictionary is just two curly braces: {} )
room_counts = {}

# ==========================================
# PHASE 2: THE MATRIX (PARSING STDIN)
# ==========================================

# Problem 2: Group Size
# Read the first line of standard input, convert it to an integer, and save it to `K`.
K = int(input())

# Problem 3: The Room List
# We need to read the second line, split it by spaces, and turn them all into integers.
# I will give you this line so we can focus strictly on the dictionary logic!
rooms = list(map(int, input().split()))

# ==========================================
# PHASE 3: THE COUNTING PROCESS
# ==========================================

# Problem 4: The Loop
# Write a for-loop that goes through every single `room` inside the `rooms` list.
for i in rooms:

    # Problem 5: The First Visit
    # Inside the loop, check if the current `room` is NOT already a key in our `room_counts` dictionary.
    # (Hint: use the `not in` keyword)
    if i not in room_counts:
        
        # Problem 6: Adding to the Registry
        # If it's not in there, this is our first time seeing it! 
        # Create a new entry in the dictionary for this `room`, and set its value to 1.
        room_counts[i] = 1

    # Problem 7: The Repeat Visit
    # Write an `else:` block for when the room IS already in the dictionary.
    else:
        
        # Problem 8: Updating the Count
        # We've seen this room before! Look up the current `room` in the dictionary, 
        # and increase its value by 1 (using += 1).
        room_counts[i] += 1

# ==========================================
# PHASE 4: FINDING THE CAPTAIN
# ==========================================

# Problem 9: Inspecting the Register
# Our dictionary is now full of room numbers and their counts!
# We need to check both the key and the value. 
# Write a for-loop that unpacks both.
for room, count in room_counts.items():

    # Problem 10: The Captain's Room
    # Inside the loop, write an if-statement checking if the `count` is exactly equal to 1.
    if count == 1:
        
        # Problem 11: The Output
        # If the count is 1, print the `room` number!
        print(room)
        
        # Problem 12: Efficiency
        # Since there is only one Captain, once you print the room, you don't need to keep searching.
        # Use the `break` keyword to stop the loop immediately.
        break