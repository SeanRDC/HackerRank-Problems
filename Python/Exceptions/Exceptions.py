# Integer-divides a by b for each test case, catching ZeroDivisionError and ValueError
# to print 'Error Code:' with the exception message instead of crashing.

T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as div:
        print(f"Error Code: {div}")
    except ValueError as val:
        print(f"Error Code: {val}")