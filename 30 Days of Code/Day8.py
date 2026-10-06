# Builds a phone book dictionary from n name/number pairs, then answers name queries
# until end of input, printing name=number or 'Not found'.

phone_book = {}

n = int(input())
for i in range(n):
    inputs = input().split()
    key = inputs[0]
    value = int(inputs[1])
    phone_book[key] = value

while True:
    try:
        query = input()
        if query in phone_book:
            print(f'{query}={phone_book[query]}')
        else:
            print('Not found')
    except EOFError:
        break