def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    # Word counter per split
    for word in words:
        num_vowels = 0
        # Vowel Counter per letter
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        # Even number checker
        if num_vowels % 2 == 0:
            score += 2
        else:
            ++score
    #return score
    pass

def scores_words(words):
    word_score = []
    for i in words:
        score = 0
        for j in i:
            if is_vowel(j):
                score += 1
        word_score.append(score)
    
    new_score = []
    
    for w in word_score:
        if w % 2 == 0:
            new_score.append(2)
        else:
            new_score.append(1)
    
    return sum(new_score)

n = int(input())
words = "programming is awesome".split()
print(scores_words(words))

# Odd number of vowels per word = score 1
# Even number of vowels per word = score 2