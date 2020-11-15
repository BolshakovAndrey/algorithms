"""
C. Эффективная быстрая сортировка
Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не должно
требоваться O(n) дополнительной памяти. А у вас получится?

Формат ввода
В первой строке на вход подается число n - длина массива. n не превосходит
1000. Во второй строке через пробел записаны n чисел. Каждое из чисел по модулю
не превосходит 1000.

Формат вывода
Нужно вывести через пробел числа в отсортированном по возрастанию порядке.
https://www.geeksforgeeks.org/python-program-for-quicksort/
"""


def quicksort(array):
    if len(array) < 2:
        return array  # базовый случай: массивы с 0 и 1 элементом уже отсортированы
    else:
        # рекурсивный случай
        pivot = array[0]
        # подмассив всех элементов, меньших опорного
        less = [i for i in array[1:] if i <= pivot]
        # подмассив всех элементов, больших опорного
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    answer = quicksort(arr)
    print(*answer)
