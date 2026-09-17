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
# mylist = [input() for i in range(int(input()))]
# print(mylist)

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
        
# ==========================================
# BLOCK 2: Object-Oriented Basics
# ==========================================

# ---------------------------------------------------------
# Problem 6: Creating a Basic Class
# ---------------------------------------------------------
# To use the HTML parser, we must use classes.
# Task: Create a class named `MyParser`. 
# Inside it, write an `__init__` method (the constructor) that takes `self` 
# and prints "Parser initialized!" when called.
# Finally, create an instance (object) of this class.
#
# MOCK INPUT / EXECUTION:
# p = MyParser()
#
# EXPECTED OUTPUT:
# Parser initialized!

# Write your code for Problem 6 here:
class MyParser:
    def __init__(self):
        print("Parser initialized")
p = MyParser()

# ---------------------------------------------------------
# Problem 7: Adding a Custom Method
# ---------------------------------------------------------
# Classes have functions inside them called methods.
# Task: Create a class called `Greeter`.
# Add a method called `say_hello(self, name)` that prints "Hello, [name]".
# Create an instance of Greeter and call `say_hello("Hacker")`.
#
# EXPECTED OUTPUT:
# Hello, Hacker

# Write your code for Problem 7 here:
class Greeter:
    def say_hello(self, name):
        return f"Hello {name}"
g = Greeter()
print(g.say_hello("Hacker"))

# ---------------------------------------------------------
# Problem 8: Inheritance Basics
# ---------------------------------------------------------
# Python's HTML parser is a built-in class. We want to inherit its powers.
# Task: I have provided a base class `BaseParser` below. 
# Create a new class called `CustomParser` that INHERITS from `BaseParser`.
# You don't need to add anything inside `CustomParser` yet (just use the `pass` keyword).
# Create an instance of `CustomParser` and call the `feed_data()` method on it.
#
# MOCK INPUT (Variables provided):
class BaseParser:
    def feed_data(self):
        print("Feeding data to the engine...")

# EXPECTED OUTPUT:
# Feeding data to the engine...

# Write your code for Problem 8 here:
class CustomParser(BaseParser):
    pass
c = CustomParser()
c.feed_data()

# ---------------------------------------------------------
# Problem 9: Method Overriding
# ---------------------------------------------------------
# When parsing HTML, the base parser has default methods that do nothing. 
# We have to "override" them to make them do what we want.
# Task: Inherit from `ParentParser` (provided below) to create `ChildParser`.
# Override the `handle_tag(self)` method so that instead of printing the parent's message, 
# it prints "Child is handling the tag!"
# Create an instance of `ChildParser` and call `handle_tag()`.
#
# MOCK INPUT (Variables provided):
class ParentParser:
    def handle_tag(self):
        print("Parent is doing nothing.")

# EXPECTED OUTPUT:
# Child is handling the tag!

# Write your code for Problem 9 here:
class ChildParser(ParentParser):
    def handle_tag(self):
        print("Child is handling the tag!")
c = ChildParser()
c.handle_tag()

# ---------------------------------------------------------
# Problem 10: Overriding with Arguments
# ---------------------------------------------------------
# The actual HTML parser sends arguments to our overridden methods.
# Task: Create a class `TagPrinter` with a method `handle_starttag(self, tag, attrs)`.
# When called, it should print "Start : [tag]".
# (Don't worry about printing the attrs yet).
# Create an instance and call it with tag="div" and attrs=[('class', 'main')].
#
# MOCK INPUT / EXECUTION:
# tp = TagPrinter()
# tp.handle_starttag("div", [('class', 'main')])
#
# EXPECTED OUTPUT:
# Start : div

# Write your code for Problem 10 here:
class TagPrinter:
    def handle_starttag(self, tag, attrs):
        return f"Start : {tag}"
    
tp = TagPrinter()
print(tp.handle_starttag("div", [('class', 'main')]))

# ==========================================
# BLOCK 3: Simulating the Parser Handlers
# ==========================================

# ---------------------------------------------------------
# Problem 11: The Start Tag Handler
# ---------------------------------------------------------
# Task: Create a class `MockStart`. 
# Add a method `handle_starttag(self, tag, attrs)`.
# Inside the method, print "Start : [tag]". 
# Then, loop through `attrs` and print them in the HackerRank format 
# (-> name > value). Remember to print DIRECTLY inside the method!
#
# MOCK INPUT / EXECUTION:
# m = MockStart()
# m.handle_starttag("body", [('data-modal-target', None), ('class', '1')])
#
# EXPECTED OUTPUT:
# Start : body
# -> data-modal-target > None
# -> class > 1

# Write your code for Problem 11 here:
class MockStart:
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")

        for name, value in attrs:
            print(f"-> {name} -> {value}")

m = MockStart()
m.handle_starttag("body", [('data-modal-target', None), ('class', '1')])

# ---------------------------------------------------------
# Problem 12: The End Tag Handler
# ---------------------------------------------------------
# Task: Create a class `MockEnd`.
# Add a method `handle_endtag(self, tag)`.
# Inside the method, simply print "End   : [tag]".
# (Notice the spaces after 'End' so it aligns with 'Start' and 'Empty')
#
# MOCK INPUT / EXECUTION:
# e = MockEnd()
# e.handle_endtag("body")
#
# EXPECTED OUTPUT:
# End   : body

# Write your code for Problem 12 here:
class MockEnd:
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
e = MockEnd()
e.handle_endtag("body")

# ---------------------------------------------------------
# Problem 13: The Empty Tag Handler
# ---------------------------------------------------------
# HTML has "empty" or "self-closing" tags like <br /> or <img src="x" />.
# Task: Create a class `MockEmpty`.
# Add a method `handle_startendtag(self, tag, attrs)`.
# Inside, print "Empty : [tag]", then loop through attrs just like in Start tags.
#
# MOCK INPUT / EXECUTION:
# emp = MockEmpty()
# emp.handle_startendtag("br", [])
# emp.handle_startendtag("img", [('src', 'logo.png')])
#
# EXPECTED OUTPUT:
# Empty : br
# Empty : img
# -> src > logo.png

# Write your code for Problem 13 here:
class MockEmpty:
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} -> {value}")

emp = MockEmpty()
emp.handle_startendtag("br", [])
emp.handle_startendtag("img", [('src', 'logo.png')])

# ---------------------------------------------------------
# Problem 14: Combining the Handlers
# ---------------------------------------------------------
# Task: Create a single class `ParserSimulator` that contains all three 
# methods you just wrote: `handle_starttag`, `handle_endtag`, and `handle_startendtag`.
# Create an instance and call them in order to simulate parsing an HTML snippet.
#
# MOCK INPUT / EXECUTION:
# sim = ParserSimulator()
# sim.handle_starttag("html", [])
# sim.handle_startendtag("hr", [('class', 'divider')])
# sim.handle_endtag("html")
#
# EXPECTED OUTPUT:
# Start : html
# Empty : hr
# -> class > divider
# End   : html

# Write your code for Problem 14 here:
class ParserSimulator:
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
    
        for name, value in attrs:
            if value is None:
                value = None
            print(f"-> {name} -> {value}")
    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            if value is None:
                value = None
            print(f"-> {name} -> {value}")

sim = ParserSimulator()
sim.handle_starttag("html", [])
sim.handle_startendtag("hr", [('class', 'divider')])
sim.handle_endtag("html")

# ---------------------------------------------------------
# Problem 15: Introduction to the Real HTMLParser
# ---------------------------------------------------------
# Let's touch the real thing! Python has a built-in library for this.
# Task: 
# 1. Import it: `from html.parser import HTMLParser`
# 2. Create a class `MyRealParser` that inherits from `HTMLParser`.
# 3. Override ONLY the `handle_starttag(self, tag, attrs)` method. 
#    Make it print "Found a tag: [tag]".
# 4. Create an instance and use the built-in `.feed()` method:
#    parser.feed("<html><head><title>Test</title></head></html>")
#
# EXPECTED OUTPUT:
# Found a tag: html
# Found a tag: head
# Found a tag: title

# Write your code for Problem 15 here:
from html.parser import HTMLParser

class MyRealParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Found a tag: {tag}")
        
r = MyRealParser()
r.feed("<html><head><title>Test</title></head></html>")