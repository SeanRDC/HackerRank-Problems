# Reads n and prints the square of every integer from 0 up to n - 1.

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)