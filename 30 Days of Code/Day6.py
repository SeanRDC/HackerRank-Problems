# For each test case, slices the string into its even-indexed and odd-indexed characters
# and prints the two pieces separated by a space.

T = int(input())

for _ in range(T):
    user_input = input()
    print(user_input[0::2], user_input[1::2])