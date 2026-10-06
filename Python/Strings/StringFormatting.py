# Prints every number from 1 to n in decimal, octal, uppercase hex, and binary, right-
# aligned to the width of n in binary. The first version uses f-string format specs and
# the second uses rjust.

def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(f'{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}')

print_formatted(17)

def print_formatted2(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):

        decimal = str(i).rjust(width)
        octal = (oct(i)[2:]).rjust(width)
        hexadecimal = ((hex(i)[2:]).upper()).rjust(width)
        binary = (bin(i)[2:]).rjust(width)

        print(decimal, octal, hexadecimal, binary)

print_formatted2(17)