# ==========================================
# SET 1: THE BUILT-IN METHODS 
# ==========================================
# Let's explore Python's capitalization tools and find the trap.
# NEW CONCEPT: `.capitalize()` makes ONLY the first letter uppercase and the rest lowercase. 
# NEW CONCEPT: `.title()` makes the first letter of EVERY word uppercase.

# Problem 1: Print the result of calling `.capitalize()` on the string "hELLO".
# Expected Output: Hello
print('hELLO'.capitalize())

# Problem 2: HackerRank has a strict rule: "12abc" should stay "12abc". 
# Print the result of calling `.capitalize()` on "12abc". 
# Expected Output: 12abc (Notice it does exactly what we want! It ignores numbers.)
print('12abc'.capitalize())

# Problem 3: Let's try the `.title()` method. 
# Print the result of calling `.title()` on "chris alan".
# Expected Output: Chris Alan (Looks perfect, right? Let's check the trap in Problem 4.)
print('chris alan'.title())

# Problem 4 (THE TRAP): Print the result of calling `.title()` on "1 w 2 r 3g".
# Expected Output: 1 W 2 R 3G
# (Look at the '3G'! HackerRank wants '3g'. `.title()` sees the number 3, assumes the 'g' 
# is a new word, and capitalizes it. We CANNOT use `.title()` for this challenge!)
print("1 w 2 r 3g".title())


# ==========================================
# SET 2: THE SPACE TRAP
# ==========================================
# Since `.title()` is out, we have to split the string into a list, capitalize each word, 
# and join it back together. But there is a second trap!

# Problem 5: Create a string with MULTIPLE spaces: `s = "hello   world"`
# Split it using an empty `.split()` and print the list.
# Expected Output: ['hello', 'world']
# (Wait! Where did the extra spaces go? Empty `.split()` destroys extra spaces. 
# HackerRank will fail you if you delete their extra spaces.)
s = "hello   world"
print(s.split())

# Problem 6 (THE FIX): We can tell `.split()` to strictly cut by space characters.
# Split `s = "hello   world"` by passing a single space string into the parentheses. 
# Save it to `word_list` and print it.
# Expected Output: ['hello', '', '', 'world']
# (By doing this, Python preserves the extra spaces as empty strings!)
s = "hello   world"
word_list = s.split(' ')
print(word_list)

# Problem 7: Loop through your `word_list`. Apply `.capitalize()` to each item, 
# and append the result to a new list called `capitalized_words`. Print it.
# (Fun fact: `.capitalize()` on an empty string `""` just returns an empty string `""`, so it won't crash!)
# Expected Output: ['Hello', '', '', 'World']
capitalized_words = []
for i in word_list:
    new = i.capitalize()
    capitalized_words.append(new)

print(capitalized_words)

# Problem 8: Join your `capitalized_words` list back together using a single space delimiter. Print it.
# Expected Output: Hello   World'
print(' '.join(capitalized_words))


# ==========================================
# SET 3: THE GRAND FINALE
# ==========================================

# Problem 9 (MINI-BOSS): Compress Problems 6, 7, and 8 into a SINGLE line of code.
# Use a List Comprehension to capitalize the items, and wrap the whole thing in a `join()` method.
# Test it on `s = "chris   alan"`
# Expected Output: Chris   Alan

# Problem 10: Drop your one-line logic into the HackerRank function!

def solve(s):
    #capitalized_words = []
    #for i in s.split(' '):
        #capitalized_words.append(i.capitalize())
    #return' '.join(capitalized_words)
    
    # or
    capitalized_words = ' '.join([i.capitalize() for i in s.split(' ')])
    return capitalized_words

# Test it:
print(solve("1 w 2 r 3g"))
# Expected Output: 1 W 2 R 3g
print(solve("chris alan"))
print(solve("sean rhani dela     cruz"))