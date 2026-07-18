# ==========================================
# SET 1: THE MANUAL SLICE (THE HARD WAY)
# ==========================================
# Let's break the string into chunks manually using slicing.

# Problem 1: Create a string `s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"` and `w = 4`.
s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4
# Problem 2: Slice and print the first chunk (indices 0 to 4).
# Expected Output: ABCD
print(s[:w])

# Problem 3: Slice and print the second chunk (indices 4 to 8).
# Expected Output: EFGH
print(s[w:8])

# Problem 4: Slice and print the third chunk (indices 8 to 12).
# Expected Output: IJKL
print(s[8:12])

# Problem 5: What is the mathematical pattern of the slice?
# Answer: It's `s[i : i + w]`, where `i` jumps forward by `w` each time!


# ==========================================
# SET 2: THE SLICING LOOP
# ==========================================
# Let's automate those jumps using the step feature of `range()`.

# Problem 6: Print `len(s)`. (Expected: 26)
print(len(s))

# Problem 7: Write a `for` loop using `range(0, len(s), w)`. 
# Inside, print `i`. 
# Expected Output: 0, 4, 8, 12, 16, 20, 24
for i in range(0, len(s), w):
    print(i)

# Problem 8: Inside that same loop, print `s[i : i + w]`. 
# (Look at that, you just wrapped the text!)
for i in range(0, len(s), w):
    print(s[i : i + w])

# Problem 9: Let's store it. Create `lines = []` before the loop. 
# Inside the loop, `.append()` the slice `s[i : i + w]` to your list.
lines = []
for i in range(0, len(s), w):
    lines.append(s[i : i + w])
print(lines) 

# Problem 10: Outside the loop, join the `lines` list using a newline character: 
# `"\n".join(lines)`. Print it. You just solved the challenge manually!
print("\n".join(lines))

# ==========================================
# SET 3: THE MAGIC MODULE (THE EASY WAY)
# ==========================================
# Python has a built-in module literally called `textwrap` that does all of Set 2 for you.

# Problem 11: Import the module at the top of your code: `import textwrap`
import textwrap

# Problem 12: Use the `textwrap.wrap()` function. Pass it your string and width: 
# `textwrap.wrap(s, w)`. Save the result to a variable `wrapped_list` and print it.
# Expected Output: ['ABCD', 'EFGH', 'IJKL', 'IMNO', 'QRST', 'UVWX', 'YZ']
wrapped_list = textwrap.wrap(s, w)
print(wrapped_list)

# Problem 13: Look familiar? `textwrap.wrap()` perfectly created the list from Problem 9!
# Print `"\n".join(wrapped_list)` to see the final formatted block.
print("\n".join(wrapped_list))

# Problem 14: What if you have actual words? 
# Print `textwrap.wrap("Hello world how are you", 5)`. 
# (Notice how it smartly tries NOT to chop words in half if it doesn't have to!)
print(textwrap.wrap("Hello world how are you",5))


# ==========================================
# SET 4: THE ULTIMATE SHORTCUT
# ==========================================
# `.wrap()` returns a list that you have to join. But there is an even faster function.

# Problem 15: Call `textwrap.fill(s, w)`. Save it to `final_text` and print it.
# Expected Output: The fully formatted, multi-line string, instantly!
final_text = textwrap.fill(s, w)
print(final_text)

# Problem 16: Marvel at how the 5-line loop from Set 2 just became a single line of code.

# Problem 17: Try `textwrap.fill(s, 10)`. See how easily it adapts.
# Problem 18: Try `textwrap.fill(s, 1)`.
print(textwrap.fill(s,10))
print(textwrap.fill(s,1))


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's plug this into the HackerRank function template.

# Problem 19: Define the HackerRank function: `def wrap(string, max_width):`

# Problem 20: Inside the function, use the ultimate shortcut from Set 4 to 
# return the wrapped text. (Remember to `import textwrap` at the top of your script!)

# Test it:
# print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))