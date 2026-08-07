# ==========================================
# PHASE 1: THE ALGORITHM
# ==========================================

# Problem 1: The Function
# Define a function named `is_prime` that accepts a single integer `n`.
def is_prime(n):

    # Problem 2: The Base Cases
    # 1 is NOT prime. If n is 1, return False.
    # 2 is prime (the only even prime!). If n is 2, return True.
    # If n is any other even number (n % 2 == 0), return False.
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
        
    # Problem 3: The Optimized Limit
    # We only need to check up to the square root of n. 
    # Create a variable named `limit` and set it to the integer value of the square root of n, plus 1.
    # (Hint: int(n**0.5) + 1)
    limit = int((n**0.5) + 1)
    
    # Problem 4: The Loop
    # Write a `for` loop that uses `range` to generate numbers from 3 up to your `limit`.
    # Since we already eliminated even numbers in Problem 2, we can skip them here!
    # Make your range jump by 2 (e.g., range(3, limit, 2)).
    for i in range(3, limit, 2):
    
        # Problem 5: The Divisibility Check
        # Inside the loop, check if `n` is perfectly divisible by the current loop number (using %).
        # If it is, `n` is not prime! Return False immediately.
        if n % i == 0:
            return False
        
    # Problem 6: The Survivor
    # If the code survives the entire loop without returning False, the number is definitely prime!
    # Outside the loop, return True.
    return True    

# ==========================================
# PHASE 2: THE MATRIX (PARSING)
# ==========================================

# Problem 7: The Master Loop
# Read the number of test cases `T`.
# Write a loop that runs `T` times.
T = int(input())
for _ in range(T):

    # Problem 8: The Execution
    # Read the next integer and pass it into your `is_prime` function.
    # If it returns True, print "Prime". Otherwise, print "Not prime".
    N = is_prime(int(input()))
    if N == True:
        print("Prime")
    else:
        print("Not prime")