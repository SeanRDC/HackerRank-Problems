# Difference keeps a private list of numbers, and computeDifference stores the absolute
# difference between the largest and smallest values in maximumDifference.

class Difference:

    def __init__(self, a):

        self.__elements = a

        self.maximumDifference = 0

    def computeDifference(self):

        min_val = min(self.__elements)

        max_val = max(self.__elements)

        diff = abs(max_val - min_val)

        self.maximumDifference = diff

if __name__ == '__main__':

    a = [int(e) for e in input().split()]

    print(a)

    d = Difference(a)

    d.computeDifference()

    print(d.maximumDifference)