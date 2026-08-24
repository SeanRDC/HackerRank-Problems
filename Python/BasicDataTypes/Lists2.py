# ==========================================
# SET 1: BASIC LIST METHODS (0 & 1 ARGUMENT)
# ==========================================

# Problem 1: Create an empty list called `my_list`. Use `.append()` to add 9, and then append 5. Print the list.
# Expected Output: [9, 5]
my_list = []
my_list.append(9)
my_list.append(5)
print(my_list)

# Problem 2: Use the `.remove()` method to delete the first occurrence of 5 from your list. Print the list.
# Mock Input: my_list = [9, 5]
# Expected Output: [9]
my_list.remove(5)
print(my_list)

# Problem 3: Append 10, then append 2 to your list. Use the `.sort()` method to sort it in ascending order. Print the list.
# Mock Input: my_list = [9, 10, 2]
# Expected Output: [2, 9, 10]
my_list.append(10)
my_list.append(2)
my_list.sort()
print(my_list)

# Problem 4: Use the `.reverse()` method to flip the list. Then use `.pop()` to remove the last item. Print the list.
# Mock Input: my_list = [2, 9, 10]
# Expected Output: [10, 9] (Because reversed is [10, 9, 2], and pop removes 2)
my_list.reverse()
my_list.pop()
print(my_list)

# Problem 5 (MINI-BOSS: COMBINE 1-4):
# Starting with an empty list `boss_list = []`, execute these exact commands in order:
# append 1, append 3, append 2, sort, reverse, pop, remove 3. 
# Print the final list.
# Expected Output: [2]
boss_list = []
boss_list.append(1)
boss_list.append(3)
boss_list.append(2)
boss_list.sort()
boss_list.reverse()
boss_list.pop()
boss_list.remove(3)
print(boss_list)

# ==========================================
# SET 2: THE INSERT METHOD & SPATIAL AWARENESS
# ==========================================

# Problem 6: The .insert(index, element) method puts an item at a specific spot. 
# Insert the number 99 at index 1 in the list below. Print the list.
my_list = [10, 20, 30]
# Expected Output: [10, 99, 20, 30]
my_list.insert(1, 99)
print(my_list)

# Problem 7: Insert the number 88 at index 0 (the very beginning). Notice how it shifts everything else to the right!
# Mock Input: my_list = [10, 99, 20, 30]
# Expected Output: [88, 10, 99, 20, 30]
my_list.insert(0, 88)
print(my_list)

# Problem 8: If you insert an item at an index larger than the list's length, it acts exactly like an append. 
# Insert 77 at index 100. Print the list.
my_list = [1]
# Expected Output: [1, 77]
my_list.insert(100, 77)
print(my_list)

# Problem 9: Pop the last item from `my_list`, then insert it back at index 0. Print the list.
my_list = [5, 6, 7]
# Expected Output: [7, 5, 6]
popped_element = my_list.pop()
my_list.insert(0, popped_element)
print(my_list)

# Problem 10 (MINI-BOSS: COMBINE 6-9):
# Start with `boss_list = []`. 
# insert 0 5 (insert 5 at index 0)
# insert 1 10 (insert 10 at index 1)
# insert 0 6 (insert 6 at index 0)
# Print the list. (This matches the first 4 steps of the HackerRank sample!)
# Expected Output: [6, 5, 10]
boss_list = []
boss_list.insert(0, 5)
boss_list.insert(1, 10)
boss_list.insert(0, 6)
print(boss_list)

# ==========================================
# SET 3: PARSING VARIABLE-LENGTH COMMANDS
# ==========================================
# The commands have different lengths (e.g., "sort" vs "insert 0 5"). We need a smarter parser!

# Problem 11: Split the string "sort". Save the first word to `cmd`. Print `cmd`.
raw = "sort"
# Expected Output: sort
cmd = raw.split()
print(cmd[0])

# Problem 12: Split the string "append 5". Save the first word to `cmd`. 
# Use a list slice `[1:]` to grab everything AFTER the command. Save it to `args_list`. Print `args_list`.
raw = "append 5"
# Expected Output: ['5']
cmd = raw.split()
args_list = cmd[1:]
print(args_list)

# Problem 13: Split "insert 0 5". Get the `args_list` using the `[1:]` slice. 
# Use list comprehension (or map) to convert `args_list` into a list of actual integers. Print the integers.
raw = "insert 0 5"
# Expected Output: [0, 5]
cmd = raw.split()
args_list = list(map(int, cmd[1:]))
print(args_list)

# Problem 14: Combine it! Write a generic 3-line parser for ANY command length.
# 1. split the input. 2. cmd = split[0]. 3. args = list(map(int, split[1:]))
# Test it on `raw = "pop"`. Print `cmd` and `args`. (Notice args will just be an empty list [] !)
raw = "pop"
# Expected Output: pop, []
cmd = raw.split()
split = cmd[0]
args = list(map(int, cmd[1:]))
print(split, args)

# Problem 15 (MINI-BOSS: PARSING ENGINE):
# Loop through the list of strings below. Use your 3-line parser from Problem 14 on each string.
# Print an f-string for each: f"Command: {cmd}, Arguments: {args}"
commands = ["insert 0 5", "sort", "remove 6"]
# Expected Output:
# Command: insert, Arguments: [0, 5]
# Command: sort, Arguments: []
# Command: remove, Arguments: [6]
for i in commands:
    split_list = i.split()
    cmd = split_list[0] 
    args = list(map(int, split_list[1:]))
    print(f'Command: {cmd}, Arguments: {args}')


# ==========================================
# SET 4: THE *ARGS UNPACKER & THE "PRINT" TRAP
# ==========================================

# Problem 16: THE TRAP! If you use `getattr()` like we did in the last challenge, it will crash on the "print" command. 
# Why? Because `.print()` is NOT a list method! 
# Write an `if` statement: if cmd == "print", just `print(my_list)`.
cmd = "print" 
my_list = [6, 5, 10]
# Expected Output: [6, 5, 10]
if cmd == 'print':
    print(my_list)

# Problem 17: We can unpack our `args` list directly into a function using the `*` operator!
# If cmd == "insert", execute `my_list.insert(*args)`. (Python will unpack [0, 5] into index 0, element 5).
cmd = "insert"
args = [0, 5]
my_list = [10]
# Expected Output (when printing my_list): [5, 10]
if cmd == 'insert':
    my_list.insert(*args)
print(my_list)

# Problem 18: If cmd != "print", use `getattr(my_list, cmd)(*args)` to execute it dynamically! 
# Test this dynamically on the "append" command. 
cmd = "append"
args = [9]
my_list = [5, 10]
# Expected Output (when printing my_list): [5, 10, 9]
if cmd != 'print':
    getattr(my_list, cmd)(*args)
print(my_list)

# Problem 19: Test your `getattr` line on a command with ZERO arguments. Python handles the empty `*args` perfectly!
cmd = "reverse"
args = []
my_list = [5, 10, 9]
# Expected Output (when printing my_list): [9, 10, 5]
getattr(my_list, cmd)(*args)
print(my_list)

# Problem 20 (THE GRAND FINALE):
# Put it all together! 
# 1. Initialize `ans = []`.
# 2. Get the number of loops `N`.
# 3. Start your loop.
# 4. Parse the input into `cmd` and `args` (your 3-line parser).
# 5. if cmd == "print", print the list.
# 6. else, use `getattr(ans, cmd)(*args)` to execute it!
# Test it against HackerRank's Sample Input 0!
# insert, append, remove, pop, reverse, sort

N = int(input())
ans = []

for i in range(N):
    command = input().lower()
    split_values = command.split()
    cmd = split_values[0]
    args = list(map(int, split_values[1:]))

    if cmd == 'print':
        print(ans)
    else:
        getattr(ans, cmd)(*args)
