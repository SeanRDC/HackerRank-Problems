# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing ---
# Input reads Line 1: N = 5, X = 3
# Loop runs 3 times (for 3 subjects).
# Subject 1 parses to list of floats: [89.0, 90.0, 78.0, 93.0, 80.0]
# (Matrix continues building...)

# --- Matrix State ---
# scores_matrix = [
#   [89.0, 90.0, 78.0, 93.0, 80.0],
#   [90.0, 91.0, 85.0, 88.0, 86.0],
#   [91.0, 92.0, 83.0, 89.0, 90.5]
# ]

# --- The Zip Engine ---
# zip(*scores_matrix) dynamically unpacks the 3 lists and groups index by index.

# --- Loop Iteration 1 ---
# Yields Tuple: (89.0, 90.0, 91.0)
# Evaluates total: sum() -> 270.0
# Evaluates length: len() -> 3
# Evaluates average: 270.0 / 3 -> 90.0
# Formats string: "90.0"
# Console Prints: 90.0

# --- Loop Iteration 2 ---
# Yields Tuple: (90.0, 91.0, 92.0)
# Evaluates total: sum() -> 273.0
# Evaluates length: len() -> 3
# Evaluates average: 273.0 / 3 -> 91.0
# Formats string: "91.0"
# Console Prints: 91.0

# (Process continues for all 5 students)
N, X = map(int, input().split())
scores_matrix = []
for _ in range(X):
    n = list(map(float, input().split()))
    scores_matrix.append(n)

for i in zip(*scores_matrix):
    print(f"{sum(i)/len(i):.1f}")