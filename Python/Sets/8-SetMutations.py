# ==========================================
# SET 1: PARSING THE INPUT
# ==========================================

# MINI-LESSON: READING AND MAPPING
# HackerRank feeds us data line by line using input().
# If a line has multiple numbers separated by spaces (e.g., "1 2 3"), we use:
# map(int, input().split()) to split the text and convert each piece into an integer.
# We can then wrap that in set() to build our mathematical set!

if __name__ == '__main__':
    # Problem 1: Read the first line (the number of elements in set A).
    # We don't actually need to use this number, but we MUST read it so HackerRank 
    # moves down to the next line.
    # Create a variable named `num_A` and set it to int(input())
    num_A = int(input())
    
    # Problem 2: Read the second line (the actual elements of set A).
    # Create a variable named `A`. 
    # Assign it: set(map(int, input().split()))
    A = set(map(int, input().split()))
    
    # Problem 3: Read the third line (the number of operations we need to perform).
    # Create a variable named `N` and set it to int(input())
    N = int(input())
    

# ==========================================
# SET 2: THE COMMAND LOOP & GETATTR
# ==========================================

# MINI-LESSON: GETATTR()
# If you have a string variable `cmd = "update"`, you can't just type `A.cmd()`. 
# Python will look for a function literally named "cmd" and crash.
# Instead, you use `getattr(object, string_name)`.
# Example: getattr(A, cmd)(other_set) evaluates to exactly A.update(other_set)

    # Problem 4: Write a `for` loop that repeats `N` times.
    # (Hint: for _ in range(N): )
for _ in range(N):
    
        # Problem 5: Inside the loop, read the first line of the operation.
        # This line looks like "intersection_update 10".
        # We only care about the first word.
        # Create a variable named `command_name` and set it to input().split()[0]
        command_name = input().split()[0]
        
        # Problem 6: Read the second line of the operation (the elements of the other set).
        # Create a variable named `other_set`.
        # Assign it exactly like you did in Problem 2: set(map(int, input().split()))
        other_set = set(map(int, input().split()))
        
        # Problem 7: Apply the mutation using our secret weapon!
        # Write: getattr(A, command_name)(other_set)
        getattr(A, command_name)(other_set)
        
    # Problem 8 (MASTER PROBLEM):
    # Step completely out of the loop.
    # We need to output the sum of all elements remaining in set A.
    # Python has a built in function for this! Write: print(sum(A))
print(A)
print(sum(A))