# Builds each row by mirroring a slice of the alphabet around its first letter, joins it
# with dashes, and centers it to the widest row. The top half is then reversed to make
# the bottom half.

import string

def print_rangoli(size):
    letters = string.ascii_lowercase[:size]
    master_row = '-'.join(letters[::-1] + letters[1:])
    width = len(master_row)
    rows = []

    for i in range(size -1, -1, -1):
        left_side = letters[i:][::-1]
        right_side = letters[i+1:]
        row_string = '-'.join(left_side + right_side)
        center_row = row_string.center(width, '-')
        rows.append(center_row)

    bottom_half = rows[:-1][::-1]

    final_rangoli = rows + bottom_half
    print('\n'.join(final_rangoli))

n = int(input())
print_rangoli(n)