# Bubble sorts the array while counting swaps, stopping early when a full pass makes no
# swaps. It then prints the swap count and the first and last elements.

import sys
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    total_swaps = 0

    for i in range(n):
        current_swaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                total_swaps += 1
                current_swaps += 1
        if current_swaps == 0:
            break

    print(f"Array is sorted in {total_swaps} swaps.")

    print(f"First Element: {a[0]}")

    print(f"Last Element: {a[-1]}")