# Walks through the string giving Kevin the positions that start with a vowel and Stuart
# the ones that start with a consonant, scoring each by the number of substrings from
# that position, then prints the winner.

def minion_game(string):

    vowels = 'AEIOU'

    kevin_score = 0
    stuart_score = 0

    length = len(string)

    for i in range(length):
        char = string[i]

        if char in vowels:

            kevin_score = length - i

        else:
            stuart_score = length - i

    if stuart_score > kevin_score:

        print(f"Stuart {stuart_score}")

    elif kevin_score > stuart_score:

        print(f"Kevin {kevin_score}")

    else:
        print("Draw")

if __name__ == '__main__':

    s = input()

    minion_game(s)