# n - количество ступенек
n = int(input())
arr = [int(p) for p in input().split(' ')]


def steps(array):
    # если в списке нет 0 -> True
    if 0 not in array:
        return "True"

    # если в списке первый 0 -> False
    if array[0] == 0:
        return "False"
    # если ноль есть внутри списка смотрим на предыдущее значение
    res = bool(True)
    for i in range(len(array)):
        if not res:
            break
        if array[i] == 0:
            res = zero_i(array, i)

    return res


def zero_i(array, i):
    step = 1
    res = 0
    # Значение перед i не равно 0?
    while array[i - step]:
        if array[i - step] >= step:
            res = True
        else:
            res = False
            step += 1
    return res

print(steps(arr))
