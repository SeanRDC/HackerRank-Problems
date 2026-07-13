# ==========================================
# SET 1: THE INPUT STRING TRAP
# ==========================================

# Problem 1: Split this string by spaces into a list of strings.
# my_string = "2 3 6 6 5"
my_string = "2 3 6 6 5"
print(my_string.split())

# Problem 2: Use a list comprehension to convert this list of strings into a list of integers.
string_scores = ['2', '3', '6', '6', '5']
converted = []
for i in string_scores:
    integer = int(i)
    converted.append(integer)
print(converted)

# List comprehension
converted = [int(i) for i in string_scores]
print("List: ", converted)

# Problem 3: Do the exact same thing, but use Python's built-in map() function and list() instead of a comprehension. (HackerRank loves this).
string_scores = ['2', '3', '6', '6', '5']
map = map(int, string_scores)
print(list(map))

# Problem 4: Combine input(), split(), and your integer conversion into a single line of code.
my_string = map(int, input().split())

# ==========================================
# SET 2: THE DUPLICATE TRAP
# ==========================================

# Problem 5: Create a list of integers with duplicate numbers.
# my_scores = [2, 3, 6, 6, 5]

# Problem 6: Convert my_scores into a 'set' to instantly destroy all duplicates.

# Problem 7: A set doesn't support indexing. Convert that set back into a standard list.

# Problem 8: Combine the duplicate removal (set) and list conversion into a single line.


# ==========================================
# SET 3: FINDING THE RUNNER-UP (METHOD 1: SORTING)
# ==========================================

# Problem 9: You have a unique list of scores. Sort them from lowest to highest.
# unique_scores = [2, 3, 5, 6]

# Problem 10: Sort the same list, but backwards (from highest to lowest).

# Problem 11: Using bracket indexing, grab the first item (the champion) from your highest-to-lowest list.

# Problem 12: Using bracket indexing, grab the second item (the runner-up) from your highest-to-lowest list.


# ==========================================
# SET 4: FINDING THE RUNNER-UP (METHOD 2: MAX & REMOVE)
# ==========================================

# Problem 13: You have a unique list of scores. Find the highest number using Python's max() function.
# unique_scores = [2, 3, 5, 6]

# Problem 14: Remove that maximum number from the list entirely using the .remove() method.

# Problem 15: Now find the max() of the remaining list. (This is your runner-up!)


# ==========================================
# SET 5: THE HACKERRANK ENVIRONMENT
# ==========================================

# Problem 16: HackerRank gives you 'n' (the number of scores) on the first line. Capture it with input().

# Problem 17: Do you actually need to use 'n' anywhere in your Python logic to solve this? (Answer as a comment).

# Problem 18: Capture the second line of input (the scores) and turn it into a list of integers (Combine Problem 4).

# Problem 19: Apply the duplicate trap fix (Set 2) to your new list of integers.

# Problem 20: THE FINAL EXAM! 
# Put it all together. Read the inputs, remove the duplicates, find the runner-up, and print it!