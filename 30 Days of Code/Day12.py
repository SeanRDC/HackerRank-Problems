# Student inherits the name and ID fields from Person and adds a list of scores.
# calculate averages the scores and maps the average to a letter grade.

class Person:
    def __init__(self, firstName, lastName, idNumber):

        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):

        print(f"Name: {self.lastName}, {self.firstName}")

        print(f"ID: {self.idNumber}")

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):

        super().__init__(firstName, lastName, idNumber)

        self.scores = scores

    def calculate(self):

        total = sum(self.scores)

        count = len(self.scores)

        a = total / count

        if a >= 90 and a <=100:
            return 'O'

        elif a >= 80 and a < 90:
            return 'E'
        elif a >= 70 and a < 80:
            return 'A'
        elif a >= 55 and a < 70:
            return 'P'
        elif a >= 40 and a < 55:
            return 'D'
        else:
            return 'T'

if __name__ == '__main__':
    n =  input().split()
    firstName = n[0]
    lastName = n[1]
    idNum = n[2]

    num_scores = int(input())
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print(f"Grade: {s.calculate()}")