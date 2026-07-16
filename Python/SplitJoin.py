def split_and_join(line):
    """ Function that splits and joins string """
    splitted = line.split()
    return '-'.join(splitted)

# Problem 1: CSV to TSV (Comma-Separated to Tab-Separated)
# You have a string of comma-separated values. Split it on the comma `,`
# and join it back together using a tab `\t` as the delimiter.
# Mock Input: "apple,banana,orange"
# Expected Output: apple	banana	orange
def csv_to_tsv(s):
    csv = s.split(',')
    return '\t'.join(csv)

print(csv_to_tsv("apple,banana,orange"))

# Problem 2: Path Converter (Windows to Mac/Linux)
# You have a Windows file path using backslashes `\`. 
# Split the string on the double-backslash `\\` and join it using a forward slash `/`.
# (Note: In Python, a single backslash is an escape character, so we use `\\` to represent it in code).
# Mock Input: "C:\\Users\\Admin\\Documents"
# Expected Output: C:/Users/Admin/Documents
def path_converter(s):
    path = s.split(r'\\')
    return '/'.join(path)

print(path_converter(r"C:\\Users\\Admin\\Documents"))

# Problem 3: The Yoda Translator (Reverse Word Order)
# Split a sentence into a list of words. Reverse that list (using `[::-1]`), 
# and join it back together with a space.
# Mock Input: "I am ready to learn Python"
# Expected Output: Python learn to ready am I
def reverser(s):
    norm = s.split()
    rev = norm[::-1]
    return ' '.join(rev)

print(reverser("I am ready to learn Python"))

# Problem 4: Acronym Generator (Combine with List Comprehension!)
# Given a string of words, split them into a list. 
# Use a list comprehension to grab the first letter (`[0]`) of each word.
# Finally, join those letters together with NO spaces `""`.
# Mock Input: "National Aeronautics Space Administration"
# Expected Output: NASA
def acronym(s):
    words = s.split()
    first_letter = [i[0] for i in words]
    return ''.join(first_letter)

print(acronym("National Aeronautics Space Administration"))

# Problem 5 (MINI-BOSS): The Space Cleaner
# When you use `.split()` and leave the parentheses completely empty, it has a superpower:
# it automatically targets and destroys ALL extra whitespace, tabs, and newlines! 
# Take a messy string, `.split()` it (with no arguments), and join it back with a single space `" "`.
# Mock Input: "This    is   a    very       messy     string"
# Expected Output: This is a very messy string
def space_cleaner(s):
    return ' '.join(s.split())

print(space_cleaner("This    is   a    very       messy     string"))
    