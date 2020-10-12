matrix = [(1, 2, 3), (0, 2,  6), (7, 4, 1), (2, 7, 0)]

for row in matrix:
    print(row)

print("\n")

t_matrix = zip(*matrix)

for row in t_matrix:
    print(row)
