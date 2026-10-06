# Three ways to swap the case of every letter in a string: a manual loop, a list
# comprehension joined back together, and the built-in swapcase method.

def swap_case_loop(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    print(result)

swap_case_loop('Pythonist 2')

def swap_case_join(s2):
    result = [i.lower() if i.isupper() else i.upper() for i in s2]
    print("".join(result))

swap_case_join('Pythonist 2')

def swap_case_hack(s3):
    print(s3.swapcase())

swap_case_hack('Pythonist 2')