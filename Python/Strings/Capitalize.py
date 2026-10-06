# Splits the string on single spaces so the original spacing is preserved, capitalizes
# each piece, and joins them back together.

def solve(s):

    capitalized_words = ' '.join([i.capitalize() for i in s.split(' ')])
    return capitalized_words

print(solve("1 w 2 r 3g"))
print(solve("chris alan"))
print(solve("sean rhani dela     cruz"))