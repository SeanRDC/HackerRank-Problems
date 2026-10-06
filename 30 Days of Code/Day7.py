# Reads an array of integers and prints it in reverse order by slicing with a step of -1
# and unpacking the result into print.

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(*arr[::-1])