# (10 ** i) // 9 produces a number made of i ones, and multiplying it by i turns it into
# the digit i repeated i times for each row of the triangle.

for i in range(1, int(input())):
    print(((10 ** i) // 9) * i)