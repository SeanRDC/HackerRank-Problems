# Builds a Student namedtuple from the header row so MARKS can be read by name whatever
# the column order, then prints the average mark to two decimal places.

from collections import namedtuple

total_students = int(input())
column_headers = input().split()
Student = namedtuple('Student', column_headers)

total_marks = 0

for _ in range(total_students):
    row_data = input().split()
    current_student = Student(*row_data)
    total_marks += int(current_student.MARKS)

average = total_marks / total_students
print(f"{average:.2f}")