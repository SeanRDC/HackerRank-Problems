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

# ==========================================
# BLOCK 2: Building the Handlers
# ==========================================

# ---------------------------------------------------------
# Problem 6: The Method Version of the Helper
# ---------------------------------------------------------
# Task: Let's turn your helper function into a class method.
# Create a class called `MockParser`.
# Add a method called `print_elements(self, tag, attrs)`.
# Put your exact logic from Problem 3 inside this method.
#
# (No execution needed yet, just define the class and method)

# Write your code for Problem 6 here:
class MockParser:
    def print_elements(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")


# ---------------------------------------------------------
# Problem 7: The Start Tag Handler
# ---------------------------------------------------------
# Task: Inside your `MockParser` class, add a new method: 
# `handle_starttag(self, tag, attrs)`.
# Instead of writing the loop again, simply CALL your helper method from 
# inside this method using `self.print_elements(tag, attrs)`.
#
# (No execution needed yet, just add the method to the class)

# Write your code for Problem 7 here (or add to your class in Problem 6):
    def handle_starttag(self, tag, attrs):
        self.print_elements(tag, attrs)


# ---------------------------------------------------------
# Problem 8: The Empty Tag Handler
# ---------------------------------------------------------
# Task: Inside your `MockParser` class, add a new method: 
# `handle_startendtag(self, tag, attrs)`.
# Just like you did in Problem 7, simply call `self.print_elements(tag, attrs)`.
#
# (No execution needed yet, just add the method)

# Write your code for Problem 8 here (or add to your class in Problem 6):
    def handle_startendtag(self, tag, attrs):
        self.print_elements(tag, attrs)


# ---------------------------------------------------------
# Problem 9: The End Tag Ignorer
# ---------------------------------------------------------
# In this specific HackerRank challenge, we DO NOT care about end tags at all.
# If we don't override the end tag method, the parser might do something we don't want.
# Task: Inside your `MockParser` class, add `handle_endtag(self, tag)`.
# Since we want it to do absolutely nothing, just put the `pass` keyword inside it.
#
# (No execution needed yet, just add the method)

# Write your code for Problem 9 here (or add to your class in Problem 6):
    def handle_endtag(self, tag):
        pass


# ---------------------------------------------------------
# Problem 10: Testing the Mock Parser
# ---------------------------------------------------------
# Task: You should now have a complete `MockParser` class with 4 methods.
# Create an instance of `MockParser`.
# Call `.handle_starttag("head", [])`.
# Call `.handle_endtag("head")`.
# Call `.handle_startendtag("br", [('class', 'clear')])`.
#
# EXPECTED OUTPUT:
# head
# br
# -> class > clear

# Write your code for Problem 10 here:
m = MockParser()
m.handle_starttag("head", [])
m.handle_endtag("head")
m.handle_startendtag("br", [('class', 'clear')])