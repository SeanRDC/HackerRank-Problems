# Cuts the string into chunks of length k and prints each chunk with its repeated
# characters removed, first with a manual loop and then with dict.fromkeys.

def merge_the_tools(string, k):

    for i in range(0, len(string), k):
        chunk = string[i : i + k]
        unique = ""
        for j in chunk:
            if j not in unique:
                unique += j
        print(unique)
    for i in range(0, len(string), k):
        chunk = string[i : i + k]
        my_dict = dict.fromkeys(chunk)
        print("".join(my_dict))

merge_the_tools('AABCAAADA', 3)