# split_and_join splits a line on whitespace and rejoins it with hyphens. The functions
# after it are extra split/join practice: CSV to TSV, path conversion, word reversal,
# acronyms, and space cleanup.

def split_and_join(line):
    """ Function that splits and joins string """
    splitted = line.split()
    return '-'.join(splitted)

def csv_to_tsv(s):
    csv = s.split(',')
    return '\t'.join(csv)

print(csv_to_tsv("apple,banana,orange"))

def path_converter(s):
    path = s.split(r'\\')
    return '/'.join(path)

print(path_converter(r"C:\\Users\\Admin\\Documents"))

def reverser(s):
    norm = s.split()
    rev = norm[::-1]
    return ' '.join(rev)

print(reverser("I am ready to learn Python"))

def acronym(s):
    words = s.split()
    first_letter = [i[0] for i in words]
    return ''.join(first_letter)

print(acronym("National Aeronautics Space Administration"))

def space_cleaner(s):
    return ' '.join(s.split())

print(space_cleaner("This    is   a    very       messy     string"))