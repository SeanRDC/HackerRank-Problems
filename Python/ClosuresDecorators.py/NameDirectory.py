# The person_lister decorator sorts the people by age and applies the decorated function
# to each one, so name_format only has to build a single 'Mr.' or 'Ms.' name.

import operator

def person_lister(f):
    def inner(people):
        sorted_names = sorted(people, key=lambda x: int(x[2]))
        new_list = []
        for i in sorted_names:
            new_list.append(f(i))
        return new_list
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')