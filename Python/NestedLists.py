# ==========================================
# SET 1: BUILDING THE ROSTER (NESTED LISTS)
# ==========================================
def pass_problem():
# Problem 1: Create an empty list called `roster`.
    roster = []

# Problem 2: Append a nested list representing one student to `roster`.
# Mock Input: name = "Harry", score = 37.21
# Expected Output of roster: [['Harry', 37.21]]
    roster.append(['Harry', 37.21])

# Problem 3: Append a second student to `roster`.
# Mock Input: name = "Berry", score = 37.21
# Expected Output of roster: [['Harry', 37.21], ['Berry', 37.21]]
    roster.append(['Berry', 37.21])
    print(roster)

# Problem 4: Write a `for` loop that runs `n` times. Inside the loop, take two inputs 
# (a string for name, a float for grade), and append them as a pair to `roster`.
# Mock Input: 
# 2
# Tina
# 37.2
# Akriti
# 41.0
# Expected Output of roster: [['Tina', 37.2], ['Akriti', 41.0]]
    n = int(input())

    for i in range(n):
        name = input()
        grade = float(input())
        roster.append([name, grade])
    print(roster)

# ==========================================
# SET 2: EXTRACTING THE GRADES
# ==========================================

# Use this mock roster for Sets 2, 3, and 4:
    roster = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

# Problem 5: Using bracket indexing, print only the grade of the first student in `roster`.
# Expected Output: 37.21
    print(roster[0][1])

# Problem 6: Create an empty list called `all_grades`. Loop through `roster` and append ONLY the grades to it.
# Expected Output: [37.21, 37.21, 37.2, 41.0, 39.0]
    all_grades = []
    for i in roster:
        all_grades.append(i[1])
        
    print(all_grades)

# Problem 7: Do the exact same thing as Problem 6, but compress it into a single list comprehension!
    all_grades = [i[1] for i in roster]
    print(all_grades)

# ==========================================
# SET 3: FINDING THE TARGET SCORE
# ==========================================

# Problem 8: Your `all_grades` list has duplicates. Convert it to a set to destroy them.
# Expected Output (order may vary): {41.0, 37.2, 37.21, 39.0}
    convert_set = set(all_grades)

# Problem 9: Convert that set back into a list, and sort it from lowest to highest.
# Expected Output: [37.2, 37.21, 39.0, 41.0]
    convert_list = list(convert_set)
    convert_list.sort()
    print(convert_list)

# Problem 10: Grab the second item from your sorted list and save it as `target_score`.
# Expected Output: 37.21
    target_score = convert_list[1]
    print(target_score)
pass

# Problem 11: Combine Problems 7, 8, 9, and 10 to find the `target_score` in as few lines as possible.
roster = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

all_grades = [i[1] for i in roster]
convert = list(set(all_grades))
convert.sort()
target_score = convert[1]
print(target_score)

# ==========================================
# SET 4: THE HUNT (MATCHING SCORE TO NAMES)
# ==========================================

# Problem 12: Create an empty list called `second_lowest_students`.
second_lowest_students = []

# Problem 13: Write a `for` loop that iterates through every `student` in `roster`.
# Problem 14: Inside that loop, write an `if` statement to check if the student's grade equals your `target_score`.
# Problem 15: If the grade matches, append the student's NAME (not their grade) to `second_lowest_students`.
# Expected Output of second_lowest_students: ['Harry', 'Berry']
for i in roster:
    if i[1] == target_score:
        second_lowest_students.append(i[0])

print(second_lowest_students)

# Problem 16: Rewrite Problems 12-15 as a single list comprehension with an `if` statement at the end!
second_lowest_students = [i[0] for i in roster if i[1] == target_score]
print(second_lowest_students)

# ==========================================
# SET 5: THE GRAND FINALE (SORT & PRINT)
# ==========================================

# Problem 17: Take your `second_lowest_students` list and sort it alphabetically.
# Expected Output: ['Berry', 'Harry']

# Problem 18: Write a simple `for` loop to print each name in your sorted list on a new line.
# Expected Output:
# Berry
# Harry

# Problem 19: Instead of a loop, use the string `.join()` method to print the sorted list with newline characters ('\n').

# Problem 20: THE FINAL EXAM!
# Put it all together. Read `n`, loop to build the roster, find the target score, find the matching names, sort them, and print them!