# ==========================================
# SET 1: FILTERING THE FILES
# ==========================================
def passable():
    # MINI-LESSON: THE MODULO OPERATOR (%)
    # The `%` operator gives you the remainder of division. 
    # If `10 % 5 == 0`, it means 10 divides evenly by 5. We will use this to check if a file can be parallelized!

    # Here is the test case from the example in the image:
    files = [4, 1, 3, 2, 8]
    numCores = 4
    limit = 1

    def minTime(files, numCores, limit):
        # Problem 1: Create a variable `total_time` and set it to 0.
        total_time = 0
        
        # Problem 2: Create an empty list named `parallel_files` to hold the files we CAN parallelize.
        parallel_files = []
        
        # Problem 3: Write a `for` loop that iterates through each `f` in `files`.
        for f in files:
        
            # Problem 4: Inside the loop, write an `if` statement to check if `f` is evenly divisible by `numCores`.
            # (Hint: use the modulo operator: f % numCores == 0)
            if f % numCores == 0:
            
                # Problem 5: If it is evenly divisible, append `f` to the `parallel_files` list.
                parallel_files.append(f)
                
            # Problem 6: Write an `else` statement for when the file cannot be divided.
            else:
            
                # Problem 7: If it cannot be divided, we MUST run it on a single core. 
                # Increment `total_time` by `f`.
                total_time += f
                
        # Problem 8 (MASTER PROBLEM 1): 
        # Step out of the loop. Let's verify our filter works by returning both variables for now.
        # Write: return total_time, parallel_files
        return total_time, parallel_files    

    # ==========================================
    # TEST CASE VERIFICATION
    # ==========================================
    test_time, test_list = minTime(files, numCores, limit)
    print(f"Time from un-parallelizable files: {test_time}")
    print(f"Files waiting to be parallelized: {test_list}")

    # EXPECTED OUTPUT: 
    # Time from un-parallelizable files: 6  (Because 1, 3, and 2 could not be divided by 4)
    # Files waiting to be parallelized: [4, 8]

    # ==========================================
    # SET 2: THE GREEDY SORT
    # ==========================================

    # Here is where we left off:
    files = [4, 1, 3, 2, 8]
    numCores = 4
    limit = 1

    def minTime(files, numCores, limit):
        total_time = 0
        parallel_files = []
        
        for f in files:
            if f % numCores == 0:
                parallel_files.append(f)
            else:
                total_time += f
                
        # Problem 9: Sort the `parallel_files` list in REVERSE order (largest to smallest).
        # Hint: You can use the built-in .sort(reverse=True)
        parallel_files.sort(reverse=True)
        
        # Problem 10: Write a `for` loop that iterates through each `f` in `parallel_files`.
        for f in parallel_files:
        
            # Problem 11: Write an `if` statement to check if we still have a `limit` greater than 0.
            if limit > 0:
            
                # Problem 12: If we do, we use a coupon! Divide `f` by `numCores` and add it to `total_time`.
                # Note: Use integer division (//) so it stays a whole number!
                use = f // numCores
                total_time += use 
                
                # Problem 13: We used a coupon, so subtract 1 from `limit`.
                limit -= 1
                
            # Problem 14: Write an `else` block for when we run out of coupons (limit is 0).
            else:
            
                # Problem 15: We have to pay full price. Add `f` to `total_time`.
                total_time += f
                
        # Problem 16 (MASTER PROBLEM 2):
        # Step completely out of the loop and `return total_time`.
        return total_time
        
    # ==========================================
    # TEST CASE VERIFICATION
    # ==========================================
    print(f"Minimum time required: {minTime(files, numCores, limit)}")

    # EXPECTED OUTPUT: 
    # Minimum time required: 12
pass
# ==========================================
# ASSEMBLE YOUR FINAL FUNCTION BELOW:
# ==========================================
files = [4, 1, 3, 2, 8]
numCores = 4
limit = 1

def minTime(files, numCores, limit):
    total_count = 0
    parallel = []
    
    for i in files:
        if i % numCores == 0:
            parallel.append(i)
        else:
            total_count += i
    
    parallel.sort(reverse=True)
    
    for j in parallel:
        if limit > 0:
            use = j // numCores
            total_count += use
            limit -= 1
        else:
            total_count += j
    return total_count

        

print(f"Final Minimum time required: {minTime(files, numCores, limit)}")
# EXPECTED OUTPUT: 
# Minimum time required: 12