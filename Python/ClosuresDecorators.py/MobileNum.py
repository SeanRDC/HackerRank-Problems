# The wrapper decorator keeps the last 10 digits of every number and rewrites it as '+91
# xxxxx xxxxx' before passing the list on to sort_phone, which prints it sorted.

def wrapper(f):
    def fun(l):
        new_list = []
        for i in l:
            clean = i[-10:]
            new_list.append(f"+91 {clean[:5]} {clean[5:]}")
        return f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
