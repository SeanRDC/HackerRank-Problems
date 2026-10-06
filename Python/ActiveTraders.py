# Counts each customer's trades in a dictionary, keeps the customers responsible for at
# least 5% of all trades, and returns their names sorted alphabetically.

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