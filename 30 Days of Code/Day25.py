# is_prime rules out 1 and even numbers, then tests only odd divisors up to the square
# root of n. The driver prints 'Prime' or 'Not prime' for each test case.

def is_prime(n):

    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    limit = int((n**0.5) + 1)

    for i in range(3, limit, 2):

        if n % i == 0:
            return False

    return True    

T = int(input())
for _ in range(T):

    N = is_prime(int(input()))
    if N == True:
        print("Prime")
    else:
        print("Not prime")