# ==========================================
# SET 1: DICTIONARY BASICS (RETRIEVING DATA)
# ==========================================

# Problem 1: Print the list of scores belonging to the key 'Krishna'.
# Mock Input: student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0]}
# Expected Output: [67.0, 68.0, 69.0]

# Problem 2: Create a variable called `query_name` and set it to 'Malika'. 
# Print the scores for that student using `query_name` as the dictionary key.
# Mock Input: student_marks = {'Malika': [52.0, 56.0, 60.0]}
# Expected Output: [52.0, 56.0, 60.0]

# Problem 3: Extract Malika's list of scores using `query_name` and save it to a variable called `active_scores`. Print `active_scores`.
# Mock Input: query_name = 'Malika', student_marks = {'Malika': [52.0, 56.0, 60.0]}
# Expected Output: [52.0, 56.0, 60.0]


# ==========================================
# SET 2: LIST MATH (SUM AND LENGTH)
# ==========================================

# Problem 4: Using a `for` loop, add up all the numbers in `active_scores` and print the total.
# Mock Input: active_scores = [52.0, 56.0, 60.0]
# Expected Output: 168.0

# Problem 5: Delete that loop. Calculate the sum using Python's built-in `sum()` function and print it.
# Mock Input: active_scores = [52.0, 56.0, 60.0]
# Expected Output: 168.0

# Problem 6: Find out how many scores are in the `active_scores` list using the built-in `len()` function.
# Mock Input: active_scores = [52.0, 56.0, 60.0]
# Expected Output: 3

# Problem 7: Calculate the average by dividing the sum by the length. Save it as `average_score` and print it.
# Mock Input: sum = 168.0, length = 3
# Expected Output: 56.0


# ==========================================
# SET 3: THE FORMATTING TRAP (2 DECIMAL PLACES)
# ==========================================

# Problem 8: Try using the built-in `round(number, 2)` function to round `average_score` to 2 decimal places. Print it.
# Mock Input: average_score = 56.0
# Expected Output: 56.0 (Notice how round() FAILS to add the trailing zero we need!)

# Problem 9: Format the number to exactly 2 decimal places using an f-string (e.g., f"{variable:.2f}").
# Mock Input: average_score = 56.0
# Expected Output: 56.00

# Problem 10: Change `average_score` to 26.5. Print it using the same f-string formatting.
# Mock Input: average_score = 26.5
# Expected Output: 26.50

# Problem 11: Change `average_score` to 33.333333. Print it using the same f-string formatting.
# Mock Input: average_score = 33.333333
# Expected Output: 33.33


# ==========================================
# SET 4: UNPACKING HACKERRANK'S MAGIC STUB
# ==========================================

# Problem 12: HackerRank reads input as a single string. Split this mock input string into a list.
# Mock Input: mock_input = "Harsh 25 26.5 28"
# Expected Output: ['Harsh', '25', '26.5', '28']

# Problem 13: Assign your split list to two variables: `name` and `*line`. Print both variables.
# Mock Input: my_list = ['Harsh', '25', '26.5', '28']
# Expected Output for `name`: 'Harsh'
# Expected Output for `line`: ['25', '26.5', '28'] (Notice how the asterisk scoops up all remaining items!)

# Problem 14: Use a list comprehension to convert the strings in `line` into floats.
# Mock Input: line = ['25', '26.5', '28']
# Expected Output: [25.0, 26.5, 28.0]

# Problem 15: Create an empty dictionary called `my_dict`. Assign your float list to the key `name`. Print the dictionary.
# Mock Input: name = 'Harsh', float_list = [25.0, 26.5, 28.0]
# Expected Output: {'Harsh': [25.0, 26.5, 28.0]}


# ==========================================
# SET 5: THE GRAND FINALE (PUTTING IT TOGETHER)
# ==========================================

# Use these mock variables representing the state AFTER HackerRank's loop runs:
# student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
# query_name = 'Harsh'

# Problem 16: Retrieve the list of scores for `query_name` and save it to `scores`.
# Expected Output: [25.0, 26.5, 28.0]

# Problem 17: Calculate the total sum of `scores`.
# Expected Output: 79.5

# Problem 18: Calculate the length of `scores`.
# Expected Output: 3

# Problem 19: Calculate the unformatted average.
# Expected Output: 26.5

# Problem 20: THE FINAL EXAM!
# Print the average formatted to exactly 2 decimal places!
# Expected Output: 26.50