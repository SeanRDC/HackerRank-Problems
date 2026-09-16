# ==============================================================================
# FUNDAMENTALS CURRICULUM: RECURSIVE DEPTH TRACKING
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE HACKERRANK TRICK (LEVEL -1)
# ---------------------------------------------------------
# Concept: Look at the boilerplate code at the very bottom: 
# `depth(tree.getroot(), -1)`
# HackerRank is passing `-1` as the starting level for the Root node. 
# But the instructions say: "Take the depth of the root as 0."
# 
# The Fix: The very first thing your function should do every time it runs 
# is increase the `level` variable by 1. 
# If it receives `-1`, it becomes `0`. If it receives `0`, it becomes `1`.

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE GLOBAL HIGH SCORE
# ---------------------------------------------------------
# Concept: Unlike the last problem where we returned a score and bubbled it up, 
# this problem uses a "Global Variable" (`maxdepth`). 
# A global variable is like a high-score board sitting outside the function. 
# 
# The Fix: After you increase the `level`, you must check: 
# "Is my current `level` higher than the global `maxdepth`?"
# If it is, overwrite `maxdepth` with your current `level`.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE RECURSIVE DIG (PASSING THE BATON)
# ---------------------------------------------------------
# Concept: Just like last time, you need a `for` loop to look at every child.
# But this time, when you call the recursive function, you aren't adding to a 
# score. You are just passing the baton (the current depth) down to the child.
#
# The Fix: Inside your loop, call `depth(child, level)`. 
# Because you already added 1 to `level` at the top of the function, the child 
# will inherit this exact level, and then add 1 to it for itself!

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    
    level += 1
    if level > maxdepth:
        maxdepth = level
    
    for child in elem:
        depth(child, level)
        
    return elem
        
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)