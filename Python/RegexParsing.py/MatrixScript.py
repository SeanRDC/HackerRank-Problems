# Builds the matrix from sample rows, reads it column by column into a single string,
# and replaces any run of symbols sitting between two alphanumeric characters with a
# space.

import re

first_multiple_input = "7 3".rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix18 = []
mock_inputs = ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]

for _ in range(n):
    matrix_item = mock_inputs[_] 
    matrix18.append(matrix_item)

print(re.sub(r'(?<=\w)\W+(?=\w)', ' ', "".join(["".join(col) for col in zip(*matrix18)])))