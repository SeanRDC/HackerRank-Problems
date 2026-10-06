# fibo builds the first n Fibonacci numbers in a list, and map applies the cube lambda
# to each of them before printing.

cube = lambda x: x**3

n = 5
def fibo(n):
    cur = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]

    for _ in range(n - len(cur)):
        cur.append(cur[-1] + cur[-2])
    return cur

print(list(map(cube, fibo(n))))