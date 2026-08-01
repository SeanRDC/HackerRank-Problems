# ==========================================
# SET 1: THE COUNTING ENGINE (Dictionaries)
# ==========================================
def passable():
    # MINI-LESSON: DICTIONARIES FOR FREQUENCY COUNTING
    # A dictionary stores data in key-value pairs. 
    # For this problem, the "key" will be the customer's name, and the "value" will be the number of times they traded.

    # 1. Here is our sample test case to work with:
    customers = ["Omega", "Alpha", "Omega", "Beta", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Beta"]

    def mostActive(customers):
        # Problem 1: We need to know the total number of trades to calculate percentages later. 
        # Create a variable named `total_trades` and set it to the length of the `customers` list.
        total_trades = len(customers)
        
        # Problem 2: Create an empty dictionary named `trade_counts` to store our tally.
        trade_counts = {}
        
        # Problem 3: We need to look at every trade. 
        # Write a `for` loop that iterates through each `name` in the `customers` list.
        for name in customers:
        
            # Problem 4: Inside the loop, write an `if` statement to check if the `name` is ALREADY in our `trade_counts` dictionary.
            if name in trade_counts:
            
                # Problem 5: If it IS already in the dictionary, increment that customer's count by 1.
                # (Hint: trade_counts[name] += 1)
                trade_counts[name] += 1
                
            # Problem 6: Write an `else` statement for when we see a customer's name for the very first time.
            else:
            
                # Problem 7: If it's their first time, add them to the dictionary and set their count to exactly 1.
                trade_counts[name] = 1
                
        # Problem 8 (MASTER PROBLEM 1): 
        # Step out of the loop. To test your engine, simply `return trade_counts` for now.
        return trade_counts

    # ==========================================
    # TEST CASE VERIFICATION
    # ==========================================
    print(f"Trade Counts: {mostActive(customers)}")

    # EXPECTED OUTPUT: 
    # Trade Counts: {'Omega': 10, 'Alpha': 8, 'Beta': 2}
    # (If you see this exact dictionary, your counting engine is flawless! Drop it here for review.)

    # ==========================================
    # SET 2: THE 5% THRESHOLD FILTER
    # ==========================================

    # MINI-LESSON: DICTIONARY ITERATION
    # To look at the data in our dictionary, we can loop through both the keys (names) and values (counts) at the same time using the `.items()` method.

    def mostActive(customers):
        total_trades = len(customers)
        trade_counts = {}
        for name in customers:
            if name in trade_counts:
                trade_counts[name] += 1
            else:
                trade_counts[name] = 1
                
        # Problem 9: Create an empty list named `active_customers` to store the names of the people who pass our 5% test.
        active_customers = []
        
        # Problem 10: Write a `for` loop that unpacks the dictionary: 
        # `for name, count in trade_counts.items():`
        for name, count in trade_counts.items():
        
            # Problem 11: Inside this loop, let's calculate the percentage.
            # Math reminder: percentage = (count / total_trades) * 100
            # Create a variable named `percentage` and assign it this math equation.
            percentage = (count / total_trades) * 100
            
            # Problem 12: Write an `if` statement checking if the `percentage` is greater than or equal to (>=) 5.
            if percentage >= 5:
            
                # Problem 13: If they meet the 5% threshold, add their `name` to the `active_customers` list.
                # (Hint: use .append())
                active_customers.append(name)
                
        # Problem 14 (MASTER PROBLEM 2): 
        # Step completely out of the loop. To test this phase, `return active_customers`.


    # ==========================================
    # TEST CASE VERIFICATION
    # ==========================================
    # customers = ["Omega", "Alpha", "Omega", "Beta", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Beta"]
    # print(f"Active Customers: {mostActive(customers)}")

    # EXPECTED OUTPUT: 
    # Alpha is 40%, Omega is 50%, Beta is 10%. All are >= 5%.
    # Active Customers: ['Omega', 'Alpha', 'Beta']

    # ==========================================
    # SET 3: ALPHABETICAL SORTING
    # ==========================================

    # MINI-LESSON: SORTING IN PYTHON
    # The problem constraints state: "Order the list alphabetically ascending by name."
    # In Python, lists have a built-in method called `.sort()` that automatically sorts the list in-place (alphabetically for strings).

    # Problem 15: We have our `active_customers` list filled with the names that passed the 5% test.
    # Right before your `return` statement (but outside the `for` loop), call the `.sort()` method on your `active_customers` list.
        active_customers.sort()

    # Problem 16 (MASTER PROBLEM 3): 
    # Make sure your `return active_customers` is at the very bottom of the function.
    # That completes the entire algorithmic logic for the `mostActive` function!
        return active_customers

    # ==========================================
    # SET 4: HACKERRANK SUBMISSION ASSEMBLY
    # ==========================================

    # MINI-LESSON: HACKERRANK'S ENVIRONMENT
    # Look at the screenshot you provided of the pre-code (image_6e5c3e.png). 
    # HackerRank already provides the `if __name__ == '__main__':` block at the bottom. 
    # They handle opening the output file, taking the `input()`, building the list, and writing the result.
    # All you need to do is provide the `def mostActive(customers):` function!

    # Problem 17: Review your complete `mostActive` function. It should have:
    # 1. Total trades calculation.
    # 2. Dictionary counting engine.
    # 3. 5% threshold filter loop.
    # 4. Alphabetical sort.
    # 5. Return statement.

    # Problem 18: Are there any `print` statements inside your `mostActive` function?
    # If so, remove them! HackerRank's pre-code handles the printing. Your function must ONLY `return` the list.

    # Problem 19: Are there any test cases or dummy variables (like `customers = [...]`) outside the function?
    # If so, delete them. The final submission should just be the `def mostActive(customers):` block.

    # Problem 20 (GRAND FINALE):
    # Assemble your clean, final `mostActive` function below!
pass

# ==========================================
# ASSEMBLE YOUR FINAL FUNCTION BELOW:
# ==========================================


def mostActive(customers):
    total_trades = len(customers)
    trade_counts = {}
    for i in customers:
        if i in trade_counts:
            trade_counts[i] += 1
        else:
            trade_counts[i] = 1
    active = []
    
    for i, j in trade_counts.items():
        percent = (j / total_trades) * 100
        if percent >= 5:
            active.append(i)
    active.sort()
    return active

customers = ["Omega", "Alpha", "Omega", "Beta", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Alpha", "Omega", "Beta"]
print(mostActive(customers))