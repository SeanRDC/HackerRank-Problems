# (10 ** i) // 9 produces a number made of i ones, and squaring it yields the
# palindromic row 1, 121, 12321, and so on.

for i in range(1, int(input())):
    print(((10 ** i) // 9) ** 2)