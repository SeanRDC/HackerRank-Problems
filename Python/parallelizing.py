# Files whose length is divisible by numCores can be parallelized, so the largest of
# them are divided by numCores until the limit runs out. Every other file is added at
# its full length.

files = [4, 1, 3, 2, 8]
numCores = 4
limit = 1

def minTime(files, numCores, limit):
    total_count = 0
    parallel = []

    for i in files:
        if i % numCores == 0:
            parallel.append(i)
        else:
            total_count += i

    parallel.sort(reverse=True)

    for j in parallel:
        if limit > 0:
            use = j // numCores
            total_count += use
            limit -= 1
        else:
            total_count += j
    return total_count



print(f"Final Minimum time required: {minTime(files, numCores, limit)}")