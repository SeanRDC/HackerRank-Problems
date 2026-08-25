# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing ---
# input() receives string: "Sorting1234"

# --- The Sorting Engine ---
# sorted() iterates character by character, passing each to get_priority().
# get_priority('S') -> Returns Tuple: (1, 'S')
# get_priority('g') -> Returns Tuple: (0, 'g')
# get_priority('1') -> Returns Tuple: (2, '1')
# get_priority('2') -> Returns Tuple: (3, '2')

# Python compares the tuples: 
# (0, 'g') is prioritized over (1, 'S').
# If priorities match (e.g., (0, 'g') and (0, 'i')), Python breaks the tie 
# using the character itself ('g' comes before 'i' alphabetically).

# --- Final Assembly ---
# sorted() returns: ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
# "".join() binds it together.
# Console Prints: ginortS1324
s = input()
def get_prio(s):
    if s.isupper():
        return(1, s)
    elif s.islower():
        return(0, s)
    elif s.isdigit() and int(s) % 2 == 1:
        return(2, s)
    elif s.isdigit() and int(s) % 2 == 0:
        return(3, s)

print(''.join(sorted(s, key=get_prio)))