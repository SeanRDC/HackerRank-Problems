# ==========================================
# SET 1: DICTIONARY BASICS (RETRIEVING DATA)
# ==========================================

# Problem 1: Print the list of scores belonging to the hardcoded key 'Krishna'.
# Mock Input: student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0]}
# Expected Output: [67.0, 68.0, 69.0]
student_marks = {
    'krishna': [67.0, 68.0, 69.0],
    'Arjun': [70.0, 98.0, 63.0]
}
print(student_marks['krishna'])

# Problem 2: Create a variable called `query_name` and set it to 'Malika'. 
# Print the scores for that student by passing `query_name` into the dictionary brackets.
# Mock Input: student_marks = {'Malika': [52.0, 56.0, 60.0]}
# Expected Output: [52.0, 56.0, 60.0]
student_marks = {'Malika': [52.0, 56.0, 60.0]}
query_name = 'Malika'
print(query_name)

# Problem 3: Extract Malika's list of scores using `query_name` and save it to a new variable called `active_scores`. Print `active_scores`.
# Mock Input: query_name = 'Malika', student_marks = {'Malika': [52.0, 56.0, 60.0]}
# Expected Output: [52.0, 56.0, 60.0]
active_scores = student_marks[query_name]
print(active_scores)

# Problem 4: Using bracket indexing, print the VERY FIRST score inside your `active_scores` list.
# Mock Input: active_scores = [52.0, 56.0, 60.0]
# Expected Output: 52.0
print(active_scores[0])

# Problem 5 (MINI-BOSS: COMBINE 1-4): 
# Given the dictionary and query_name below, extract the student's list of scores, save it to a variable, and print the LAST score in their list using negative indexing.
# Mock Input: student_marks = {'Harsh': [25.0, 26.5, 28.0]}, query_name = 'Harsh'
# Expected Output: 28.0
student_marks = {'Harsh': [25.0, 26.5, 28.0]}
query_name = 'Harsh'
active_scores = student_marks[query_name]
print(active_scores[-1])

# ==========================================
# SET 2: MATH & AVERAGES
# ==========================================

# Problem 6: Calculate the sum of `my_list` using Python's built-in `sum()` function and print it.
# Mock Input: my_list = [52.0, 56.0, 60.0]
# Expected Output: 168.0

# Problem 7: Find out how many numbers are in `my_list` using the built-in `len()` function.
# Mock Input: my_list = [52.0, 56.0, 60.0]
# Expected Output: 3

# Problem 8: Calculate the average by dividing a hardcoded sum (168.0) by a hardcoded length (3). Print it.
# Mock Input: s = 168.0, l = 3
# Expected Output: 56.0

# Problem 9: Print the average of this new list by dividing `sum(new_list)` by `len(new_list)`.
# Mock Input: new_list = [25.0, 26.5, 28.0]
# Expected Output: 26.5

# Problem 10 (MINI-BOSS: COMBINE 6-9): 
# Write a 2-line script that calculates and prints the exact average of `boss_list`. 
# Mock Input: boss_list = [70.0, 98.0, 63.0]
# Expected Output: 77.0


# ==========================================
# SET 3: THE FORMATTING TRAP (2 DECIMAL PLACES)
# ==========================================

# Problem 11: Try using `round(number, 2)` on `avg_score`. Print it. Notice it FAILS to add the trailing zero!
# Mock Input: avg_score = 56.0
# Expected Output: 56.0 

# Problem 12: Format `avg_score` to exactly 2 decimal places using an f-string: f"{variable:.2f}". Print it.
# Mock Input: avg_score = 56.0
# Expected Output: 56.00

# Problem 13: Change `avg_score` to 26.5. Print it using the EXACT SAME f-string formatting.
# Mock Input: avg_score = 26.5
# Expected Output: 26.50

# Problem 14: Change `avg_score` to 33.333333. Print it using the EXACT SAME f-string formatting.
# Mock Input: avg_score = 33.333333
# Expected Output: 33.33

# Problem 15 (MINI-BOSS: COMBINE 11-14 + SET 2): 
# Calculate the average of `format_list`, and print the result completely formatted to 2 decimal places using an f-string.
# Mock Input: format_list = [26.0, 28.0, 30.0]
# Expected Output: 28.00


# ==========================================
# SET 4: UNPACKING HACKERRANK'S MAGIC STUB
# ==========================================

# Problem 16: HackerRank inputs arrive as one string. Split this mock string into a list of strings.
# Mock Input: mock_input = "Harsh 25 26.5 28"
# Expected Output: ['Harsh', '25', '26.5', '28']

# Problem 17: Assign your split list to two variables: `name` and `*line`. Print `name` and `line`.
# Mock Input: my_list = ['Harsh', '25', '26.5', '28']
# Expected Output for `name`: 'Harsh'
# Expected Output for `line`: ['25', '26.5', '28'] (The asterisk scoops up all remaining items!)

# Problem 18: Use a list comprehension to convert the strings inside `line` into a list of floats.
# Mock Input: line = ['25', '26.5', '28']
# Expected Output: [25.0, 26.5, 28.0]

# Problem 19: Create an empty dictionary called `my_dict`. Assign your float list to the key `name`. Print the dict.
# Mock Input: name = 'Harsh', float_list = [25.0, 26.5, 28.0]
# Expected Output: {'Harsh': [25.0, 26.5, 28.0]}

# Problem 20 (THE GRAND FINALE: COMBINE EVERYTHING!):
# HackerRank already ran their loop. You are given a fully populated dictionary and a query_name.
# Find the student's scores, calculate their average, and print it formatted to EXACTLY 2 decimal places.
# Mock Input: 
# student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
# query_name = 'Arjun'
# Expected Output: 77.00