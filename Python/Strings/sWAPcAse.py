# ==========================================
# SET 1: STRING METHODS (CASE CHECKING)
# ==========================================

# Problem 1: You can force a string to lowercase using `.lower()`. 
# Print the lowercase version of "HELLO".
# Expected Output: hello
print('HELLO'.lower())

# Problem 2: You can force a string to uppercase using `.upper()`. 
# Print the uppercase version of "world".
# Expected Output: WORLD
print('world'.upper())

# Problem 3: You can check if a letter is uppercase using `.isupper()`. 
# This returns True or False. Print the result of `"H".isupper()`.
# Expected Output: True
print('H'.isupper())

# Problem 4: Print the result of `"h".isupper()`.
# Expected Output: False
print('h'.isupper())

# Problem 5 (MINI-BOSS: COMBINE 1-4):
# Create `char = "A"`. Write an `if / else` block:
# If `char` is uppercase, print its lowercase version. 
# Else, print its uppercase version. 
# Expected Output: a
char = 'A'

if char.isupper():
    print(char.lower())
else:
    print(char.upper())


# ==========================================
# SET 2: BUILDING STRINGS (THE LOOPS)
# ==========================================

# Problem 6: Since strings are just lists of characters under the hood, we can loop through them!
# Loop through the string `"Cat"` and print each character.
# Expected Output: 
# C
# a
# t
string = 'Cat'
for i in string:
    print(i)
    
# Problem 7: Because strings are immutable, we change them by creating an empty string `""` and adding to it (`+=`).
# Create `new_word = ""`. Loop through `"Cat"`. Inside the loop, do `new_word += char`. Print `new_word` at the end.
# Expected Output: Cat
new_word = ""
for i in string:
    new_word += i
print(new_word)

# Problem 8: Let's swap! Loop through `"Cat"`. If `char.isupper()`, add its lowercase to `new_word`. 
# Else, add its uppercase. Print `new_word`.
# Expected Output: cAT
new_words=""
for i in string:
    if i.isupper():
        new_words += i.lower()
    else:
        new_words += i.upper()
print(new_words)

# Problem 9: What happens to symbols and numbers? 
# Print the result of `"1".isupper()`. Then print the result of `"1".islower()`.
# Expected Output: False \n False (Numbers have no case, so they always return False!)
print('1'.isupper())
print('1'.islower())

# Problem 10 (MINI-BOSS: COMBINE 6-9):
# Start with `ans = ""`. Loop through `raw = "a1B!"`. 
# If `char.isupper()`, add lower. 
# Elif `char.islower()`, add upper. 
# Else (if it's a number/symbol), add the character as-is!
# Print `ans`. 
# Expected Output: A1b!
ans = ""
raw = 'a1B!'

for char in raw:
    if char.isupper():
        ans += char.lower()
    elif char.islower():
        ans += char.upper()
    else:
        ans += char
print(ans)

# ==========================================
# SET 3: THE JOIN METHOD (THE PYTHONIC WAY)
# ==========================================
# Building strings with `+=` inside a loop is actually very slow in Python. Here is the faster way!

# Problem 11: The `.join()` method smashes a list of characters into a single string.
# Run `"".join(['P', 'y', 't', 'h', 'o', 'n'])` and print the result.
# Expected Output: Python
print("".join(['P', 'y', 't', 'h', 'o', 'n']))

# Problem 12: Let's use List Comprehension to build the list! 
# Run `[char.upper() for char in "abc"]` and print it.
# Expected Output: ['A', 'B', 'C']
swap = [i.upper() for i in "abc"]
print(swap)

# Problem 13: Combine them! Smash the list comprehension from Problem 12 into a string using `"".join(...)`. Print it.
# Expected Output: ABC
joined = "".join(swap)
print(joined)

# Problem 14: You can use "Ternary Operators" (one-line if/else statements) inside list comprehensions.
# Print the result of: `"A" if True else "B"`
# [Do This] if [Condition is True] else [Do That]
# Expected Output: A

char = 'A'

result = char.lower() if char.isupper() else char.upper()

# expanded version 

if char.isupper():
    print(char.lower())
else:
    char.upper()

print(f'result: {result}')


# Problem 15 (MINI-BOSS: COMBINE 11-14):
# Smash this list comprehension into a string: 
# `[char.lower() if char.isupper() else char.upper() for char in "aBc!"]`
# Print the final smashed string. 

result = [i.lower() if i.isupper() else i.upper() for i in "aBc!1"]
print("".join(result))
# ==========================================
# SET 4: THE GRAND FINALE
# ==========================================

# Problem 16: Turn your Mini-Boss 10 logic into a function called `swap_case_loop(s)`.
# Have it return the final string.
def swap_case_loop(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    print(result)

# Problem 17: Call `swap_case_loop("Pythonist 2")` and print the result.
# Expected Output: pYTHONIST 2
swap_case_loop('Pythonist 2')

# Problem 18: Write a second function called `swap_case_join(s)`. 
# Make it return the exact one-liner you built in Problem 15, replacing `"aBc!"` with the variable `s`.
def swap_case_join(s2):
    result = [i.lower() if i.isupper() else i.upper() for i in s2]
    print("".join(result))
    
swap_case_join('Pythonist 2')

# Problem 19: The Python Secret! 
# Because this is such a common task, Python actually has a built-in string method that does all of this instantly.
# Print `"HackerRank".swapcase()`. 
# Expected Output: hACKERrANK
def swap_case_hack(s3):
    print(s3.swapcase())

swap_case_hack('Pythonist 2')

# Problem 20 (THE GRAND FINALE):
# Now you know THREE ways to solve this challenge (a for-loop, a join comprehension, and the built-in method).
# Complete the HackerRank editor function:
# def swap_case(s):
#     # return the swapped string using your favorite method!
# Test it against Sample Input 0: 'HackerRank.com presents "Pythonist 2".'