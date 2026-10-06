# factorial multiplies n by the factorial of n - 1 until it reaches the base case of 1.
# fibonacci uses the same recursive idea, summing the two previous terms.

def factorial(n):

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Series of numbers where each number is the sum of the two numbers that came before it.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(4))
