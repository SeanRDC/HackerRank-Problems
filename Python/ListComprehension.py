# ==========================================
# SET 1: THE INCLUSIVE LOOP (1D)
# ==========================================
def pass_problem():
# PROBLEM 1: The Vertical Inputs
# INSTRUCTIONS: Call input() twice. Convert both to integers. Assign to x and y. Print them using an f-string.
# MOCK INPUT:
# 1
# 2
# EXPECTED OUTPUT: x is 1, y is 2
    x = int(input())
    y = int(input())
    print(f'x is {x}, y is {y}')

# PROBLEM 2: The Inclusive Range
# INSTRUCTIONS: Set x = 1. Write a for loop using range() that prints 0 and then 1. Remember range(x) stops at x-1.
# MOCK INPUT: (None)
# EXPECTED OUTPUT:
# 0
# 1
    x = 1
    for i in range(x + 1):
        print(i)

# PROBLEM 3: The Traditional Append
# INSTRUCTIONS: Set x = 2. Create an empty list called 'coords'. Loop from 0 to x (inclusive). Append each number to the list. Print the list.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [0, 1, 2]
    x = 2
    coords = []

    for i in range(x + 1):
        coords.append(i)
    print(coords)

# PROBLEM 4: The 1D List Comprehension
# INSTRUCTIONS: Set x = 2. Do exactly what you did in Problem 3, but in ONE line of code using a list comprehension: [expression for item in iterable]. Print it.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [0, 1, 2]
    x = 2

    coords = [i for i in range(x + 1)]
    print(coords)

# PROBLEM 5: SYNTHESIS (The 1D Comp)
# INSTRUCTIONS: Get an integer input for x. Print a list of numbers from 0 to x using a 1-line list comprehension.
# MOCK INPUT: 3
# EXPECTED OUTPUT: [0, 1, 2, 3]
    x = int(input())
    coords = [i for i in range(x + 1)]
    print(coords)


# ==========================================
# SET 2: GOING MULTIDIMENSIONAL (2D & 3D)
# ==========================================

# PROBLEM 6: The Nested Loop (2D)
# INSTRUCTIONS: Set x = 1 and y = 1. Write a loop for 'i' from 0 to x, and inside it, a loop for 'j' from 0 to y. Print f'{i} {j}'.
# MOCK INPUT: (None)
# EXPECTED OUTPUT:
# 0 0
# 0 1
# 1 0
# 1 1
    x = 1
    y = 1
    for i in range(x + 1):
        for j in range(y + 1):
            print(f'{i} {j}')

# PROBLEM 7: The 2D List Comprehension
# INSTRUCTIONS: Set x = 1 and y = 1. Create a 2D comprehension: [i for i in range(...) for j in range(...)]. Print the list.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [0, 0, 1, 1]
    x = 1
    y = 1
    coords = [i for i in range(x + 1) for j in range(y + 1)]
    print(coords)

# PROBLEM 8: Generating Coordinates [i, j]
# INSTRUCTIONS: Set x = 1, y = 1. Modify Problem 7. Instead of just putting 'i' in the list, put the list pair [i, j] into the list. Print it.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0], [0, 1], [1, 0], [1, 1]]
    x = 1
    y = 1
    coords = [[i, j] for i in range(x + 1) for j in range(y + 1)]
    print(coords)

    # other version
    coords2 = []

    for i in range(x + 1):
        for j in range (y + 1):
            coords2.append([i, j])
    print(coords2)

# PROBLEM 9: Adding the Third Dimension (3D)
# INSTRUCTIONS: Set x = 1, y = 1, z = 1. Write a traditional nested loop with THREE levels (i, j, k). Append the coordinate [i, j, k] to an empty list. Print the list.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    x = 1
    y = 1
    z = 1
    coords3 = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                coords3.append([i, j, k])
    print(coords3)

# PROBLEM 10: SYNTHESIS (The 3D Grid)
# INSTRUCTIONS: Set x = 1, y = 1, z = 1. Condense Problem 9 into a single 1-line list comprehension. Print it.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    x = 1
    y = 1
    z = 1
    coords = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    print(coords)


# ==========================================
# SET 3: FILTERING WITH CONDITIONALS
# ==========================================

# PROBLEM 11: The != Operator
# INSTRUCTIONS: Set n = 2 and my_sum = 3. Write an if statement checking if my_sum is NOT EQUAL to n. If true, print 'Valid!'.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: Valid!
    n = 2
    my_sum = 3

    if my_sum != n:
        print('Valid!')

# PROBLEM 12: Appending with a Condition
# INSTRUCTIONS: Set n = 2. Create an empty list. Loop i from 0 to 3. If i is NOT EQUAL to n, append it to the list. Print the list.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [0, 1, 3]
    n = 2
    e_list = []

    for i in range(4):
        if i != n:
            e_list.append(i)
    print(e_list)

# PROBLEM 13: Filtering a 1D Comprehension
# INSTRUCTIONS: Set n = 2. Convert Problem 12 into a 1-line list comprehension by adding an 'if' at the end: [i for i in range(...) if i != n]. Print it. [expression for item in iterable if condition]
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [0, 1, 3]
    n = 2
    e_list = [i for i in range(4) if i !=n]
    print(e_list)

# PROBLEM 14: Filtering by Sum (i + j != n)
# INSTRUCTIONS: Set x = 1, y = 1, n = 1. Write a 2D list comprehension for [i, j]. Add a filter at the end so it only includes coordinates where (i + j) is not equal to n. Print it.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0], [1, 1]]
    x = 1
    y = 1
    n = 1
    coords = [[i, j] for i in range(x + 1) for j in range(y + 1) if (i + j) != n]
    print(coords)
    # expanded form
    coords2 = []
    for i in range(x + 1):
        for j in range(y + 1):
            total = i + j
            if total != n:
                coords2.append([i, j])
    print(coords2)


# PROBLEM 15: SYNTHESIS (Filtered Coordinates)
# INSTRUCTIONS: Set x = 1, y = 1, z = 1, n = 2. Write a 3D list comprehension for [i, j, k]. Filter so it only includes coordinates where (i + j + k) != n. Print it.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    x = 1
    y = 1
    z = 1
    n = 2
    coords = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(coords)
pass

# ==========================================
# SET 4: THE HACKERRANK ENVIRONMENT
# ==========================================

# PROBLEM 16: Stacking Four Inputs
# INSTRUCTIONS: Write four lines of code to get integer inputs for x, y, z, and n. Print them all in an f-string.
# MOCK INPUT: 
# 1
# 1
# 1
# 2
# EXPECTED OUTPUT: x=1, y=1, z=1, n=2
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(f"x={x}, y={y}, z={z}, n={n}")

# PROBLEM 17: Lexicographic Order Check
# INSTRUCTIONS: Good news: Python's nested loops automatically generate lists in "lexicographic increasing order". You don't need to sort anything. To pass this step, just print 'Order is automatic!'.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: Order is automatic!
print("Order is automatic!")

# PROBLEM 18: Printing a Raw List of Lists
# INSTRUCTIONS: Set my_list = [[0, 0, 0], [1, 1, 1]]. Just print(my_list). Do NOT use the asterisk (*). HackerRank wants the brackets this time.
# MOCK INPUT: (None)
# EXPECTED OUTPUT: [[0, 0, 0], [1, 1, 1]]
my_list = [[0, 0, 0], [1, 1, 1]]
print(my_list)

# PROBLEM 19: The Skeleton
# INSTRUCTIONS: Print the string 'Ready!'. (The logic is: 1. Get 4 inputs. 2. Write a 3D comprehension generating [i, j, k]. 3. Filter where i+j+k != n. 4. Print it.)
# MOCK INPUT: (None)
# EXPECTED OUTPUT: Ready!
print("Ready!")

# PROBLEM 20: THE FINAL EXAM
# INSTRUCTIONS: Combine everything! Take 4 inputs (x, y, z, n) and print the filtered 3D grid in exactly ONE print statement containing the list comprehension.
# MOCK INPUT: 
# 1
# 1
# 1
# 2
# EXPECTED OUTPUT: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coords = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) !=n]
print(coords)

# expanded form
coords2 = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            total = i + j + k
            if total != n:
                coords2.append([i, j, k])
print(coords2)