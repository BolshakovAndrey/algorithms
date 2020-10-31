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
    # Значение перед i не равно 0?
    while array[i - step] == 0:
        step += 1
    else:
        if array[i - step] > step:
            return True
        else:
            return False


print(steps(arr))
