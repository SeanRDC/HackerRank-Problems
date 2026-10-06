# Reads X rows of subject scores and uses zip(*rows) to regroup them per student,
# printing each student's average to one decimal place.

N, X = map(int, input().split())
scores_matrix = []
for _ in range(X):
    n = list(map(float, input().split()))
    scores_matrix.append(n)

for i in zip(*scores_matrix):
    print(f"{sum(i)/len(i):.1f}")