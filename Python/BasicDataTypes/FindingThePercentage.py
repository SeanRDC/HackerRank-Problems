# Stores each student's marks in a dictionary keyed by name, then averages the queried
# student's marks and prints the result with two decimal places.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_grades = student_marks[query_name]
    average = sum(student_grades) / len(student_grades)
    print(f'{average:.2f}')