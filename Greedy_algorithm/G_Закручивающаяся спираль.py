# Номер упешной отправки 38697886 30 окт 2020, 14:22:21

# k - начальный индекс строки
# m — количество строк матрицы -> индекс конца строки
# l - начальный индекс столбца
# n — количество столбцов -> индекс конечного столбца
# a - массив данных
# i - итератор

m = int(input())
n = int(input())
a = list(list(list(map(int, input().split(" ")))) for _ in range(m))


def spiralPrint(m, n, a):
    k = 0
    l = 0

    while k < m and l < n:
        for i in range(l, n):
            print(a[k][i])
        k += 1

        # Распечатать последний столбец из оставшигося столбца

        for i in range(k, m):
            print(a[i][n - 1])
        n -= 1

        # Распечатать последнюю строку из оставшейся строки

        if k < m:

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i])
            m -= 1

        # Распечатать первый столбец из оставшиеся столбцы

        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l])
            l += 1

spiralPrint(m, n, a)
