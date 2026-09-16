# ==============================================================================
# THE 20-STEP MASTERY CURRICULUM: RECURSION & XML TRAVERSAL
# ==============================================================================

# --- PHASE 1: UNDERSTANDING NODE ATTRIBUTES (THE SCORE) ---
# Problem 1: Define a function `get_attr_number(node)`.
# Problem 2: Inside the function, access the node's dictionary of attributes 
#            using the property `node.attrib`.
# Problem 3: Use Python's built-in `len()` function to calculate how many 
#            items are in that dictionary.
# Problem 4: Create a variable called `score` and assign that length to it.
# Problem 5: (Mental Check) Understand that if a node has no attributes, 
#            `len()` will safely return 0. `score` is now the node's base score.

# --- PHASE 2: UNDERSTANDING TREE ITERATION (THE CHILDREN) ---
# Problem 6: We must check if this current node has child branches. 
#            Write a `for` loop to iterate through the node.
# Problem 7: Name the iteration variable `child`. 
#            Syntax: `for child in node:`
# Problem 8: (Mental Check) What does this loop do? In ElementTree, looping 
#            directly over a node automatically gives you its DIRECT children.
# Problem 9: Inside this loop, how do we get the child's attributes? 
#            (Answer: `child.attrib`).
# Problem 10: (Mental Check) If the child has its own children (grandchildren), 
#             this single `for` loop won't see them. We need a way to dig deeper.

# --- PHASE 3: THE RECURSIVE LEAP (DIGGING DEEPER) ---
# Problem 11: Inside the `for child in node:` loop, we need to calculate the 
#             total score of that specific child (and its children).
# Problem 12: How do we do that? By calling the EXACT function we are currently 
#             writing! Type `get_attr_number(child)` inside the loop.
# Problem 13: (Mental Check) This is Recursion! The function is pausing its 
#             current job to run a fresh copy of itself on the child node.
# Problem 14: The recursive call `get_attr_number(child)` will eventually return 
#             a number (the child's total score). 
# Problem 15: We need to capture that number. Add it to our running total using 
#             the `+=` operator: `score += get_attr_number(child)`.

# --- PHASE 4: THE EXIT STRATEGY (BUBBLING UP) ---
# Problem 16: The `for` loop will run for every single direct child. 
# Problem 17: If a child has no children of its own, its `for` loop just skips, 
#             and it returns its own score. This is called the "Base Case."
# Problem 18: Once the `for` loop in our current function finishes, it means 
#             we have added the scores of all children and grandchildren.
# Problem 19: Step outside of the `for` loop (un-indent). 
# Problem 20: Write `return score` to send the final, massive tallied number 
#             back to whoever called the function.

import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    
    for child in node:
        score += get_attr_number(child)
    return score
        
