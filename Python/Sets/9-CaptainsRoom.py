# Counts how many times each room number appears in a dictionary and prints the one that
# appears exactly once, which is the captain's room.

room_counts = {}

K = int(input())

rooms = list(map(int, input().split()))

for i in rooms:

    if i not in room_counts:

        room_counts[i] = 1

    else:

        room_counts[i] += 1

for room, count in room_counts.items():

    if count == 1:

        print(room)

        break