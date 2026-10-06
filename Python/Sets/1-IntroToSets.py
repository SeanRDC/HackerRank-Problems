# Removes duplicate heights by converting the list to a set, then returns the average of
# the distinct values.

def average(array):
    set_co = set(array)
    return sum(set_co) / len(set_co)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)