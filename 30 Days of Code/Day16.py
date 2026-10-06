# Tries to convert the input string to an integer and print it, catching ValueError to
# print 'Bad String' when the conversion fails.

if __name__ == '__main__':
    S = input().strip()
    try:
        print(int(S))
    except ValueError:
        print("Bad String")
