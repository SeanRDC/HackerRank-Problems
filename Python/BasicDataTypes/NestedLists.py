# Stores [name, grade] pairs, finds the second lowest unique grade, and prints the names
# of every student with that grade in alphabetical order.

if __name__ == '__main__':
    roster = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        roster.append([name, score])

    all_grades = [i[1] for i in roster]
    convert = list(set(all_grades))
    convert.sort()
    target_score = convert[1]

    second_lowest_students = [i[0] for i in roster if i[1] == target_score]

    sorted_list = sorted(second_lowest_students)
    join_func = '\n'.join(sorted_list)

    print(join_func)