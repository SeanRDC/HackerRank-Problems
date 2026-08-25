# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing (Lines 1 & 2) ---
# _ = input() reads "5" and discards it.
# arr = input().split() reads the string and generates:
# arr = ["12", "9", "61", "5", "14"]

# --- Evaluation Step 1: all() ---
# Generator casts to int and checks > 0:
# int("12") > 0 -> True
# int("9") > 0 -> True
# int("61") > 0 -> True
# int("5") > 0 -> True
# int("14") > 0 -> True
# all() returns: True

# --- The AND Operator (Short-Circuit Check) ---
# Left side is True. The `and` operator MUST evaluate the right side to be sure.

# --- Evaluation Step 2: any() ---
# Generator checks string reversal:
# "12" == "21" -> False
# "9" == "9" -> True
# any() finds a True! It immediately stops iterating and returns: True

# --- Final Output (Line 3) ---
# True and True evaluates to: True
# Console Prints: True
_ = int(input())
arr = input().split()
print(all(int(i) > 0 for i in arr) and any(j == j[::-1] for j in arr))