# ==============================================================================
# FUNDAMENTALS CURRICULUM: CUSTOM SORTING & MAPPING DECORATORS
# ==============================================================================
# Goal: Write the `inner(people)` function. It needs to sort the list of lists 
# based on age (casting it to an integer first to avoid bugs), and then return 
# a new list by feeding each sorted person into the original function `f`.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: UNDERSTANDING THE DATA
# ---------------------------------------------------------

# Problem 1: The Nested List
# Concept: The boilerplate `input().split()` creates a list of strings for 
# each person, and puts them all inside a master list.
# Mock State of `people`: 
# [
#   ['Mike', 'Thomson', '20', 'M'], 
#   ['Robert', 'Bustle', '32', 'M'],
#   ['Andria', 'Bustle', '30', 'F']
# ]

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE SORTING ENGINE
# ---------------------------------------------------------

# Problem 2: The Default Sort Danger
# Concept: If you just call `sorted(people)`, Python will sort by the first 
# item (First Name). We need to tell Python to sort by the 3rd item (Age).

# Problem 3: The Custom Key 
# Concept: Just like when you built your custom `lambda` sorting key for 
# dictionaries a few sessions ago, you can pass a `key=` to `sorted()`. 

# Problem 4: The String vs Integer Trap
# Concept: Because `input().split()` makes everything a string, the age '20' is 
# a string. If you sort strings, '100' comes BEFORE '20' (because '1' is less 
# than '2'). 
# Solution: Your sorting lambda needs to look at the element at index 2, AND 
# cast it to an `int()`.
# Mock Syntax: `sorted(people, key=lambda x: int(x[2]))`

# Note on the Boilerplate: The instructions mention `operator.itemgetter(2)`. 
# While this is a cool built-in tool, it doesn't cast to integer, which makes 
# it dangerous for numbers. We will stick to our First Principles `lambda` key!

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE FACTORY ASSEMBLY LINE
# ---------------------------------------------------------

# Problem 5: The Decorator Loop
# Concept: Now you have a perfectly sorted list of people. But `name_format` (f) 
# only knows how to process ONE person at a time. 

# Problem 6: The List Comprehension Handoff
# Concept: You need to return a newly built list. Use a list comprehension to 
# loop through your newly sorted list, passing each `person` into `f`. 
# Mock Syntax: `return [f(person) for person in your_sorted_list]`

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Stage ---
# Boilerplate creates master list:
# people = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]

# --- The Interception ---
# Boilerplate tries to call `name_format(people)`.
# The `@person_lister` intercepts it, passing `people` into `inner(people)`.

# --- The Sorting (Inside `inner`) ---
# `inner` calls `sorted()` with the custom lambda key.
# It evaluates int('20'), int('32'), int('30').
# It generates the correctly ordered list:
# sorted_list = [['Mike', 'Thomson', '20', 'M'], ['Andria', 'Bustle', '30', 'F'], ['Robert', 'Bustle', '32', 'M']]

# --- The Assembly Line Handoff (Inside `inner`) ---
# `inner` loops through `sorted_list`.
# Feeds Index 0 to `f`: `f` returns "Mr. Mike Thomson"
# Feeds Index 1 to `f`: `f` returns "Ms. Andria Bustle"
# Feeds Index 2 to `f`: `f` returns "Mr. Robert Bustle"
# `inner` returns this brand new list of 3 formatted strings back to the boilerplate!

import operator

def person_lister(f):
    def inner(people):
        sorted_names = sorted(people, key=lambda x: int(x[2]))
        new_list = []
        for i in sorted_names:
            new_list.append(f(i))
        return new_list
        #return [f(i) for i in sorted_names]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')