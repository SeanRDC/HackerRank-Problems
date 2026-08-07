# =====================================================================
# THE PROBLEM: Count word occurrences and output them in the exact order 
# of their first appearance, alongside the total number of distinct words.
# THE GOAL: Use an OrderedDict (or standard dict in Python 3.7+) to track 
# frequencies while preserving chronological order.
# =====================================================================

# ---------------------------------------------------------
# PHASE 1: THE IMPORT AND SETUP
# ---------------------------------------------------------

# Problem 1: The Import
# Import `OrderedDict` from the `collections` module.
from collections import OrderedDict

# Problem 2: The Frequency Ledger
# Instantiate a new empty `OrderedDict` and assign it to a variable `word_counts`.
word_counts = OrderedDict()

# ---------------------------------------------------------
# PHASE 2: PARSING INPUT AND COUNTING
# ---------------------------------------------------------

# Problem 3: Total Words
# Read the first line of standard input, convert it to an integer, and save it to `N`.
N = int(input())

# Problem 4: The Loop
# Write a `for` loop that runs `N` times to read each word.
for _ in range(N):

    # Problem 5: Read the Word
    # Inside the loop, read the next line of input, and remove any trailing newline characters 
    # using `.strip()` or `.rstrip()`. Save it to a variable `word`.
    word = input().strip()
    
    # Problem 6: The Counting Logic (New Word)
    # Write an `if` statement to check if the `word` is NOT in `word_counts`.
    if word not in word_counts:
    
        # Problem 7: Initialize Count
        # Inside the if-block, add the word to `word_counts` with a starting value of `1`.
        word_counts[word] = 1
        
    # Problem 8: The Counting Logic (Existing Word)
    # Write an `else` block for when the word already exists in `word_counts`.
    else:
    
        # Problem 9: Increment Count
        # Inside the else-block, add `1` to the existing count for that word.
        word_counts[word] += 1
        

# ---------------------------------------------------------
# PHASE 3: FORMATTED OUTPUT
# ---------------------------------------------------------

# Problem 10: Total Distinct Words
# On the first output line, print the total number of distinct words.
# (Hint: How do you find the number of keys in a dictionary?)
print(len(word_counts.keys()))

# Problem 11: Unpacking the Occurrences
# Write a `for` loop that extracts just the *values* (the occurrence counts) from your `word_counts` dictionary.
# (Hint: use .values())
for values in word_counts.values():

# Problem 12: Printing the Counts
# Inside this loop, print each occurrence count separated by a space.
# (Hint: Use `end=" "` inside your print function!)
    print(values, end=" ")

# =====================================================================
# FINAL SUBMISSION
# SUMMARY: Assemble your import, your OrderedDict, your loop that reads 
# `N` words and updates their counts, the distinct word count print statement, 
# and the final loop that prints all counts separated by spaces.
# 
# MOCK INPUT (STDIN): 
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# 
# EXPECTED OUTPUT: 
# 3
# 2 1 1
# =====================================================================

from collections import OrderedDict
counter = OrderedDict()

N = int(input())

for _ in range(N):
    word = input().strip()
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print((len(counter.keys())))

for values in counter.values():
    print(values, end=" ")