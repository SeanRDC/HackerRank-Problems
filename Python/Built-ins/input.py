# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Line 1 ---
# input() receives string: "1 4"
# split() breaks it: ["1", "4"]
# map() casts them: [1, 4]
# Unpacking assigns: x = 1, k = 4

# --- Input Line 2 ---
# input() receives string: "x**3 + x**2 + x + 1"
# Assigns to variable: poly_str = "x**3 + x**2 + x + 1"

# --- The Evaluation Engine ---
# eval("x**3 + x**2 + x + 1") executes.
# Python checks namespace, finds x = 1.
# Executes: 1**3 + 1**2 + 1 + 1
# Evaluates to: 4

# --- The Boolean Comparison ---
# Compares evaluated result (4) to k (4).
# 4 == 4 evaluates to: True

# --- Final Output ---
# Console Prints: True
x, k = map(int, input().split())
poly_str = input()
p = eval(poly_str)
print(p == k)