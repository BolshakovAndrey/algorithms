matrix = [[1, 2, 3],
          [0, 2, 6],
          [7, 4, 1],
          [2, 7, 0]]


def get_neighbors(a, b):
    d = {(i, c): matrix[i][c] for i in range(len(matrix)) for c in range(len(matrix[0]))}
    return filter(None, [d.get(i) for i in
                         [(a, b + 1),
                          (a + 1, b),
                          (a - 1, b),
                          (a, b - 1)]])


results = get_neighbors(3, 0)
print("Соседи элемента на позиции (3,0):", list(results))
