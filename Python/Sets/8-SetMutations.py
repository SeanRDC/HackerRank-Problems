# Reads set A, then applies each named update operation to it with another set by
# calling the method dynamically with getattr, and finally prints the sum of A.

if __name__ == '__main__':
    num_A = int(input())

    A = set(map(int, input().split()))

    N = int(input())

for _ in range(N):

        command_name = input().split()[0]

        other_set = set(map(int, input().split()))

        getattr(A, command_name)(other_set)

print(A)
print(sum(A))