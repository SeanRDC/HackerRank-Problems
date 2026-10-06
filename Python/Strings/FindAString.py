# Slides a window the length of the substring across the string and counts every
# position where the slice matches, so overlapping occurrences are included.

def count_substring(string, sub_string):
    count = 0
    window = len(sub_string)

    for i in range(len(string)):
        sliced = string[i:i + window]
        if sliced == sub_string:
            count += 1
    return count

print(count_substring("ABCDCDC", "CDC"))