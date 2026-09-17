# ==========================================
# BLOCK 1: Newlines and String Classification
# ==========================================

# ---------------------------------------------------------
# Problem 1: Detecting Newlines
# ---------------------------------------------------------
# To figure out if a comment is multi-line, we have to look for newlines.
# Task: Write a loop that goes through the list `comments` below.
# If the string contains a newline character ('\n'), print "Has newline".
# Otherwise, print "No newline".
#
# MOCK INPUT:
comments = ["Just a normal comment", "A comment\nwith a line break"]
#
# EXPECTED OUTPUT:
# No newline
# Has newline

# Write your code for Problem 1 here:
import re

for text in comments:
    has = bool(re.search(r'[\r\n]', text))
    if has:
        print("Has newline")
    else:
        print("No newline")
        
# ---------------------------------------------------------
# Problem 2: The Exact Match Edge Case
# ---------------------------------------------------------
# HackerRank tells us: "Do not print data if data == '\n'".
# Task: Loop through the list `data_nodes`. 
# If the string is EXACTLY equal to '\n', print "Skip". 
# Otherwise, print "Keep".
#
# MOCK INPUT:
data_nodes = ["Hello World", "\n", "   "]
#
# EXPECTED OUTPUT:
# Keep
# Skip
# Keep

# Write your code for Problem 2 here:
for i in data_nodes:
    if i == "\n":
        print("Skip")
    else:
        print("Keep")
        
# ---------------------------------------------------------
# Problem 3: Single vs. Multi-line Classification
# ---------------------------------------------------------
# Let's combine this logic.
# Task: Write a function `classify_comment(text)` that takes a string.
# If the string contains '\n', print "Multi-line".
# If it does not contain '\n', print "Single-line".
#
# MOCK INPUT / EXECUTION:
# classify_comment("One line")
# classify_comment("Line one\nLine two")
#
# EXPECTED OUTPUT:
# Single-line
# Multi-line

# Write your code for Problem 3 here:
def classify_comment(text):
    for i in text:
        if i == "\n":
            print("New-line")
            
    if '\n' in text:
        print("Multi-line")
    else:
        print("Single-line")

classify_comment("One line")
classify_comment("Line one\nLine two")
classify_comment("\n")

# ---------------------------------------------------------
# Problem 4: Printing the Headers and Data
# ---------------------------------------------------------
# The HackerRank output format requires specific headers.
# Task: Write a function `print_data(text)` that takes a string.
# If the string is EXACTLY '\n', do nothing (use `pass` or `return`).
# Otherwise, print ">>> Data" followed by the text on the next line.
#
# MOCK INPUT / EXECUTION:
# print_data("Welcome to HackerRank")
# print_data("\n")
# print_data("End of page")
#
# EXPECTED OUTPUT:
# >>> Data
# Welcome to HackerRank
# >>> Data
# End of page

# Write your code for Problem 4 here:
def print_data(text):
    if text == "\n":
        pass
    else:
        print(f">>> Data\n{text}")
        
print_data("Welcome to HackerRank")
print_data("\n")
print_data("End of page")

# ---------------------------------------------------------
# Problem 5: The Full Comment Printer
# ---------------------------------------------------------
# Task: Write a function `print_comment(text)` that checks for newlines.
# If it has a newline, print ">>> Multi-line Comment" followed by the text.
# If it does NOT have a newline, print ">>> Single-line Comment" followed by the text.
#
# MOCK INPUT / EXECUTION:
# print_comment("This is hidden")
# print_comment("Hidden\non two lines")
#
# EXPECTED OUTPUT:
# >>> Single-line Comment
# This is hidden
# >>> Multi-line Comment
# Hidden
# on two lines

# Write your code for Problem 5 here:
def print_comment(text):
    if bool(re.search(r'[\r\n]', text)):
        print(f">>> Multi-line Comment\n{text}")
    else:
        print(f">>> Single-line Comment\n{text}")
        
print_comment("This is hidden")
print_comment("Hidden\non two lines")

# ==========================================
# BLOCK 2: Building the Handlers
# ==========================================

# ---------------------------------------------------------
# Problem 6: The Data Handler Method
# ---------------------------------------------------------
# Task: Create a class `MockData`.
# Add a method `handle_data(self, data)`.
# Inside this method, use your logic from Problem 4: 
# If data is exactly '\n', do nothing. 
# Otherwise, print ">>> Data" followed by the data on the next line.
#
# MOCK INPUT / EXECUTION:
# md = MockData()
# md.handle_data("Welcome to HackerRank")
# md.handle_data("\n")
# md.handle_data("Enjoy your stay")
#
# EXPECTED OUTPUT:
# >>> Data
# Welcome to HackerRank
# >>> Data
# Enjoy your stay

# Write your code for Problem 6 here:
class MockData:
    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            print(f">>> Data\n{data}")
            
md = MockData()
md.handle_data("Welcome to HackerRank")
md.handle_data("\n")
md.handle_data("Enjoy your stay")

# ---------------------------------------------------------
# Problem 7: The Comment Handler Method
# ---------------------------------------------------------
# Task: Create a class `MockComment`.
# Add a method `handle_comment(self, data)`.
# Inside this method, use your logic from Problem 5 (try using the `in` keyword!):
# If '\n' is in the data, print ">>> Multi-line Comment" and the data.
# Otherwise, print ">>> Single-line Comment" and the data.
#
# MOCK INPUT / EXECUTION:
# mc = MockComment()
# mc.handle_comment("Just testing")
# mc.handle_comment("Line 1\nLine 2")
#
# EXPECTED OUTPUT:
# >>> Single-line Comment
# Just testing
# >>> Multi-line Comment
# Line 1
# Line 2

# Write your code for Problem 7 here:
class MockComment:
    def handle_comment(self, data):
        if "\n" in data:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")
            
mc = MockComment()
mc.handle_comment("Just testing")
mc.handle_comment("Line 1\nLine 2")

# ---------------------------------------------------------
# Problem 8: The Combined Simulator
# ---------------------------------------------------------
# Task: Create a single class `ParserSimulator`.
# Put BOTH methods (`handle_data` and `handle_comment`) inside this class.
# Ensure they work together when called on the same object.
#
# MOCK INPUT / EXECUTION:
# sim = ParserSimulator()
# sim.handle_comment("Header comment")
# sim.handle_data("Page Content")
# sim.handle_data("\n")
#
# EXPECTED OUTPUT:
# >>> Single-line Comment
# Header comment
# >>> Data
# Page Content

# Write your code for Problem 8 here:
class ParserSimulator:
    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            print(f">>> Data\n{data}")
            
    def handle_comment(self, data):
            if "\n" in data:
                print(f">>> Multi-line Comment\n{data}")
            else:
                print(f">>> Single-line Comment\n{data}")
                
sim = ParserSimulator()
sim.handle_comment("Header comment")
sim.handle_data("Page Content")
sim.handle_data("\n")

# ---------------------------------------------------------
# Problem 9: The Shell of the Real Parser
# ---------------------------------------------------------
# Task: Let's prep the real parser.
# 1. Import `HTMLParser` from `html.parser`.
# 2. Create a class `HackerRankParser` that inherits from `HTMLParser`.
# 3. Define the two methods `handle_comment(self, data)` and `handle_data(self, data)`.
# 4. Instead of writing the logic inside them, just use the `pass` keyword for now.
# (We are just building the blueprint!)
#
# MOCK INPUT / EXECUTION:
# hp = HackerRankParser()
# print(isinstance(hp, HTMLParser))
#
# EXPECTED OUTPUT:
# True

# Write your code for Problem 9 here:
from html.parser import HTMLParser

class HackerRankParser(HTMLParser):
    def handle_comment(self, data):
        pass
    
    def handle_data(self, data):
        pass
hp = HackerRankParser()
print(isinstance(hp, HTMLParser))

# ---------------------------------------------------------
# Problem 10: Analyzing the Boilerplate
# ---------------------------------------------------------
# In HackerRank, they provide a specific way to read the input for Part 2.
# They read all N lines, add '\n' to each, and combine them into one string `html`.
# Task: Look at the string `raw_html` below. It simulates what HackerRank generates.
# Call your `ParserSimulator` (from Problem 8) manually to parse it. 
# (Call handle_comment on the first part, handle_data on the middle, etc.)
#
# MOCK INPUT / EXECUTION (Variables provided):
raw_html = "<!--Test-->\n<div>Content</div>"

# Call your simulator here manually:
#sim2 = ParserSimulator()
#sim2.handle_comment("Test")
#sim2.handle_data("\n")
#sim2.handle_data("Content")
#
# EXPECTED OUTPUT:
# >>> Single-line Comment
# Test
# >>> Data
# Content

# Write your code for Problem 10 here:
sim2 = ParserSimulator()
sim2.handle_comment("Test")
sim2.handle_data("\n")
sim2.handle_data("Content")

# ==========================================
# BLOCK 3: Final Assembly
# ==========================================

# ---------------------------------------------------------
# Problem 11: The Real Parser Implementation
# ---------------------------------------------------------
# Task: Create `MyHTMLParser` inheriting from `HTMLParser`.
# Override `handle_comment(self, data)` and `handle_data(self, data)`.
# Paste in your excellent logic from Block 2, but make sure to fix the 
# `text` vs `data` variable name bug in `handle_data`!
#
# (No execution needed, just build the complete class.)

from html.parser import HTMLParser

# Write your code for Problem 11 here:
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            print(f">>> Data\n{data}")
                
    def handle_comment(self, data):
        if "\n" in data:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")

# ---------------------------------------------------------
# Problem 12: Testing the Real Parser
# ---------------------------------------------------------
# Task: Let's test your parser from Problem 11.
# Create an instance of `MyHTMLParser`.
# Feed it this exact string: "<!--[if IE 9]>IE9-specific content\n<![endif]-->"
#
# EXPECTED OUTPUT:
# >>> Multi-line Comment
# [if IE 9]>IE9-specific content
# <![endif]

# Write your code for Problem 12 here:
n = MyHTMLParser()
n.feed("<!--[if IE 9]>IE9-specific content\n<![endif]-->")

# ---------------------------------------------------------
# Problem 13: Understanding the Boilerplate
# ---------------------------------------------------------
# In Part 1, we joined all inputs with `"".join()`. 
# But in Part 2, HackerRank does something different to preserve line breaks!
# They provide this exact boilerplate at the bottom of the challenge:
# 
# html = ""       
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'
#
# Task: Wrap that exact logic inside a function called `get_html()`.
# Have the function return the `html` string at the end.
# (This step just ensures you understand how the input string is built).

# Write your code for Problem 13 here:
def get_html(N):
    html = ""
    for i in range(N):
        html += input().rstrip()
        html += '\n'
    return html

# ---------------------------------------------------------
# Problem 14: The Final Blueprint
# ---------------------------------------------------------
# You now have all the pieces! 
# Task: Write the execution block. 
# 1. Instantiate your `MyHTMLParser`.
# 2. Call your `get_html()` function to get the input.
# 3. Feed that input to the parser.
# 4. Call `parser.close()` at the very end (this is good practice to tell 
#    the parser no more data is coming).
#
# MOCK INPUT:
# 2
# <div> Welcome to HackerRank</div>
# <!-- Single comment -->
#
# EXPECTED OUTPUT:
# >>> Data
#  Welcome to HackerRank
# >>> Single-line Comment
#  Single comment 

# Write your code for Problem 14 here:
m = MyHTMLParser()
m.feed(get_html(int(input())))
m.close()



# ---------------------------------------------------------
# Problem 15: The Victory Lap
# ---------------------------------------------------------
# Let's run the exact sample case from the HackerRank prompt.
# Task: Just copy your final, complete code (the Class + the execution block).
# You don't need to write anything new. Put it all together in one clean script 
# so it is ready to copy/paste directly into HackerRank!

# Write your final complete code for Problem 15 here:
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            print(f">>> Data\n{data}")
            
    def handle_comment(self, data):
        if "\n" in data:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()