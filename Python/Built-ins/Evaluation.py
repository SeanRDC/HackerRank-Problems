# Evaluates the input line as a Python expression with eval and prints the result if
# there is one.

result = eval(input())
if result is not None:
    print(result)
