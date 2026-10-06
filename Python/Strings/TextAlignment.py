# Practice with ljust, rjust, and center, building up the cone and belt pieces of the
# HackerRank logo by padding repeated characters.

word = "Hacker"
print(word.ljust(15, '-'))

print(word.rjust(15, '*'))

print(word.center(15, '_'))

print(word.center(20))

print('H' * 5)

c = "H"

for i in range(3):
    print((c * i).rjust(3))

for i in range(3):
    print((c*i).ljust(3))

for i in range(3):
    print((c * i).rjust(3) + c.center(1) + (c * i).ljust(3))

print('HHH'.center(6))

print("HHHHHHHHHHHHHHH".center(18))

for i in range(3):
    print(3 - i - 1)

for i in range(3):
    print((c * (3 - i - 1)).rjust(3) + c.center(1) + (c * (3 - i - 1)).ljust(3))

print("Move me".rjust(40))

for i in range(3):
    print(((c * (3 - i - 1)).rjust(3) + c.center(1) + (c * (3 - i - 1)).ljust(3)).rjust(40))

t = 5
print((c * (t * 5)).center(t * 6))