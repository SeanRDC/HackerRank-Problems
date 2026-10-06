# Counts the shoe sizes in stock with a Counter, then for each customer adds the price
# to the total and decrements that size only if it is still available.

from collections import Counter

num_shoes = int(input())

inventory = Counter((map(int, input().split())))

num_customers = int(input())

total_money = 0

for i in range(num_customers):

    size, price = map(int, input().split())

    if inventory[size] > 0:

        total_money += price
        inventory[size] -= 1
print(total_money)