# Номер успешной отпавки - 38286352

# n - количество строк матрицы.
n = int(input())
# m - число столбцов
m = int(input())
arr = list(list(list(map(int, input().split(" ")))) for _ in range(n))

res_arr = zip(*arr)
for row in res_arr:
    print(*row)
