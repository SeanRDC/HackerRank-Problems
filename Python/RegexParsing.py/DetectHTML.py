# ==========================================
# BLOCK 1: Formatting and The Helper Function
# ==========================================

# ---------------------------------------------------------
# Problem 1: Printing the Tag (No Prefix)
# ---------------------------------------------------------
# In Part 1, we printed "Start : tag". Here, we just print the tag itself.
# Task: Create a variable `tag_name = "head"`. 
# Print it exactly as it is.
#
# EXPECTED OUTPUT:
# head

# Write your code for Problem 1 here:
tag_name = "head"
print(tag_name)


# ---------------------------------------------------------
# Problem 2: Formatting the Attributes
# ---------------------------------------------------------
# Task: You've done this before! Loop through `attrs` below and print 
# them in the exact format: -> name > value
#
# MOCK INPUT:
attrs = [('type', 'application/x-flash'), ('width', '0')]
#
# EXPECTED OUTPUT:
# -> type > application/x-flash
# -> width > 0

# Write your code for Problem 2 here:
for name, value in attrs:
    print(f"-> {name} > {value}")


# ---------------------------------------------------------
# Problem 3: The Helper Function
# ---------------------------------------------------------
# Because Start tags and Empty tags require the EXACT same output in this 
# challenge, it's good practice (D.R.Y. - Don't Repeat Yourself) to write 
# the logic once in a helper function.
# Task: Create a function `print_elements(tag, attrs)`.
# Inside it, first print the tag name. Then loop through `attrs` and print them.
# (Just combine your code from Problems 1 and 2).

# Write your code for Problem 3 here:
def print_elements(tag, attrs):
    print(tag)
    for name, value in attrs:
        print(f"-> {name} > {value}")

# ---------------------------------------------------------
# Problem 4: Testing the Helper (No Attributes)
# ---------------------------------------------------------
# Task: Call your `print_elements` function from Problem 3.
# Pass in "title" as the tag, and an empty list `[]` for the attributes.
#
# EXPECTED OUTPUT:
# title

# Write your code for Problem 4 here:
print_elements("title", [])



# ---------------------------------------------------------
# Problem 5: Testing the Helper (With Attributes)
# ---------------------------------------------------------
# Task: Call your `print_elements` function from Problem 3 again.
# Pass in "param" as the tag, and `[('name', 'quality'), ('value', 'high')]` 
# as the attributes.
#
# EXPECTED OUTPUT:
# param
# -> name > quality
# -> value > high

# Write your code for Problem 5 here:
print_elements("param", [('name', 'quality'), ('value', 'high')])