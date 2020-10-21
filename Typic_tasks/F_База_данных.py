# Номер успешной отправки - 36863299

n = int(input())
# Считаем строку
full_list = [str(a) for a in input().split(' ')]
# Используем set() что бы устранить дубли
set_number = set(full_list)
# приведем множество к списку для итерации по нему
short_list = [str(a) for a in set_number]


# def diff(full, short):
#     # Скопируем список с дублями в переменную
#     result = full_list.copy()
#     for i in short:
#         # Пока не останется только искомый дубль
#         # будем искать i в из списка без дублей в списке
#         # c дубликатами
#         if i in full and i in short and len(result) > 1:
#             # если он есть и там и там удаляем его
#             result.remove(i)
#
#     return print(*result)

# 3 1 3 4 2
# diff(full_list, short_list)


# Более компактное решение с stackoverflow
# https://ru.stackoverflow.com/questions/533108/%D0%9A%D0%B0%D0%BA-%D0%BD%D0%B0%D0%B9%D1%82%D0%B8-%D0%B2%D1%81%D0%B5-%D0%B4%D1%83%D0%B1%D0%BB%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B5%D1%81%D1%8F-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-%D0%B2-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B5-%D0%B8-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%B8%D1%85-%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D0%BE%D0%B2
# counter = {}
# for elem in full_list:
#     counter[elem] = counter.get(elem, 0) + 1
# doubles = {element: count for element, count in counter.items() if count > 1}
# print(*doubles)


# еще более компактно
def test(lst):
    return {a: lst.count(a) for a in set(lst) if lst.count(a) > 1}


print(test([3, 1, 3, 4, 2]))
