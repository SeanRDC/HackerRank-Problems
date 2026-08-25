# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Boilerplate Parsing ---
# Loops 5 times parsing inputs into `arr`.
# arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
# k = 1

# --- The Sorting Engine ---
# arr.sort(key=lambda row: row[1]) executes.
# Evaluates row 1: returns 2
# Evaluates row 2: returns 1
# Evaluates row 3: returns 9
# Evaluates row 4: returns 23
# Evaluates row 5: returns 5
#
# Python sorts based on those returned keys: 1, 2, 5, 9, 23.
# Array becomes: [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]

# --- The Output Engine ---
# Loop Iteration 1:
# row = [7, 1, 0]
# print(*row) -> print(7, 1, 0)
# Console Prints: 7 1 0

# Loop Iteration 2:
# row = [10, 2, 5]
# print(*row) -> print(10, 2, 5)
# Console Prints: 10 2 5

# (Process repeats for remaining rows)
def passable():
    arr = []
    k = int(input())
    for i in range(1, 6):
        arr1 = list(map(int, input().split()))
        arr.append(arr1)

    for j in sorted(arr, key=lambda row: row[k]):
        print(*j)
pass

# Other form
arr = [list(map(int, input().split())) for i in range(1, 6)]
k = int(input())
[print(*j) for j in sorted(arr, key=lambda row: row[k])]
