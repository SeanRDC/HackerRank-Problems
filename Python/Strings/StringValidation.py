# Uses any() over the characters to print whether the string contains at least one
# alphanumeric, alphabetic, digit, lowercase, and uppercase character.

s = "qA2"
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))