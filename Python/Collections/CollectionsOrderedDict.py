# Splits each line into an item name and a price, accumulates the totals in an
# OrderedDict, and prints each item with its net price in first-seen order.

from collections import OrderedDict

ledger = OrderedDict()

N = int(input())
for _ in range(N):
    words = input().split()
    price = int(words[-1])
    item = words[:-1]
    item_name = ' '.join(item)

    if item_name not in ledger:
        ledger[item_name] = price
    else:
        ledger[item_name] += price

for key, value in ledger.items():
    print(f"{key} {value}")