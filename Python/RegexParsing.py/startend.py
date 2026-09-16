import re
m = re.search(r'\d+','1234')
print(m.end()) # 4
print(m.start()) # 0

S = input() # aaadaa
k = input() # aa

pattern = re.compile(rf'(?=({re.escape(k)}))')

matches = list(pattern.finditer(S))

if matches:
    for match in matches:
        start_index = match.start()
        end_index = start_index + len(k) - 1
        print(f"({start_index}, {end_index})")
else:
    print("(-1, -1)")



