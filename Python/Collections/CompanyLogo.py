# Counts the characters with a Counter, sorts them by descending count and then
# alphabetically, and prints the top three with their counts.

from collections import Counter

s = input().strip()

count = Counter(s).items()
sorting_key = lambda t: (-t[1], t[0])
sorted_mech = sorted(count, key=sorting_key)[:3]
for char, value in sorted_mech:
    print(f"{char} {value}")