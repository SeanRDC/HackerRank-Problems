# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Input ---
# input() receives string: "print(2 + 3)"

# --- The Execution Engine ---
# eval() receives the string.
# eval() parses the string as active Python code.
# The code triggers Python's built-in print() function.
# The math (2 + 3) is evaluated as the argument for print().

# --- Final Output ---
# Console Prints: 5
# (Script terminates seamlessly without returning 'None')
result = eval(input())
if result is not None:
    print(result)
