# ==========================================
# BLOCK 1: Inputs, Tuples, and Formatting
# ==========================================

# ---------------------------------------------------------
# Problem 1: The N-Line Reader
# ---------------------------------------------------------
# In HackerRank, you are often given a number N, followed by N lines of text. 
# Task: Write a script that reads an integer N from the user. 
# Then, use a loop to read N lines of string input. 
# Store these strings in a list and print the list.
# 
# MOCK INPUT (Type this into your terminal when testing):
# 3
# <html>
# <head>
# </head>
#
# EXPECTED OUTPUT:
# ['<html>', '<head>', '</head>']

# Write your code for Problem 1 here:
mylist = [input() for i in range(int(input()))]
print(mylist)

# ---------------------------------------------------------
# Problem 2: Joining the Pieces
# ---------------------------------------------------------
# The HTML parser likes to read everything as one giant string rather than a list of lines. 
# Task: Take the list of strings provided below and join them together 
# into a single continuous string. Print the final string.
#
# MOCK INPUT (Variables provided):
lines = ["<html>", "<head>", "</head>", "<body>", "</body>", "</html>"]
#
# EXPECTED OUTPUT:
# <html><head></head><body></body></html>

# Write your code for Problem 2 here:
print(''.join(lines))

# ---------------------------------------------------------
# Problem 3: Unpacking Tuples
# ---------------------------------------------------------
# When the HTML parser finds attributes inside a tag (like class='1'), 
# it packages them as a list of tuples: [('class', '1')].
# Task: Write a for loop that iterates over the `attributes` list below. 
# For each tuple, unpack it into two variables (name and value) 
# and print them side-by-side separated by a space.
#
# MOCK INPUT (Variables provided):
attributes = [('id', 'main'), ('class', 'container')]
#
# EXPECTED OUTPUT:
# id main
# class container

# Write your code for Problem 3 here:
for name, value in attributes:
    print(name, value)

# ---------------------------------------------------------
# Problem 4: Handling the "None" Edge Case
# ---------------------------------------------------------
# Sometimes HTML tags have attributes with no value (like <input disabled>). 
# The parser represents this as [('disabled', None)].
# Task: Loop through the `attrs_with_none` list. If the value is the 
# Python `None` data type, print the string "None". Otherwise, print the actual value.
#
# MOCK INPUT (Variables provided):
attrs_with_none = [('type', 'text'), ('disabled', None), ('required', None)]
#
# EXPECTED OUTPUT:
# text
# None
# None

# Write your code for Problem 4 here:
for name1, value1 in attrs_with_none:
    if value1 is None:
        print(None)
    else:
        print(value1)

# ---------------------------------------------------------
# Problem 5: Getting the Exact Format
# ---------------------------------------------------------
# The HackerRank problem requires a very specific output format for attributes: 
# -> attribute_name > attribute_value
# Task: Combine what you learned in Problems 3 and 4. Loop through the list below 
# and print them exactly in the HackerRank format.
#
# MOCK INPUT (Variables provided):
final_attrs = [('data-modal-target', None), ('class', '1')]
#
# EXPECTED OUTPUT:
# -> data-modal-target > None
# -> class > 1

# Write your code for Problem 5 here:
for name, value in final_attrs:
        print(f"-> {name} > {value}")