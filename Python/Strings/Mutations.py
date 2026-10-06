# Converts the string to a list, replaces the character at the given position, and joins
# the list back into a string.

def mutate_string(string, position, character):
    word_list = list(string)
    word_list[position] = character
    return ''.join(word_list)

print(mutate_string("abracadabra", 5, "k"))