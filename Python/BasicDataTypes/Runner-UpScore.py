# Removes duplicate scores with a set, deletes the maximum, and prints the new maximum
# as the runner-up. The second version does the same but reads the scores one per line.

n = int(input())
arr = map(int, input().split())

returned = list(set(arr))
maximum = max(returned)
returned.remove(maximum)
new_max = max(returned)

print(new_max)

n = int(input())

new_arr = [int(input()) for i in range(n)]

returned = list(set(new_arr))
maximum = max(returned)
returned.remove(maximum)
new_max = max(returned)

print(f'Runner-Up Score: {new_max}')
