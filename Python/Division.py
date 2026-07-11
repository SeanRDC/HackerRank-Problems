if __name__ == '__main__':
    a = int(input())
    b = int(input())

integer_division = a // b
float_division = a / b

if b == 0:
    print('Error: Cannot divide by Zero.')
else:
    print(integer_division)
    print(float_division)