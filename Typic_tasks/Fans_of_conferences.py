from collections import Counter

arr = map(int, input('Введите данные через пробел: ').split())
k = int(input('Введите количество представленных вузов: '))
c = Counter(arr).most_common(k)
print(c)
# 1 2 3 1 2 3 4 1 2 3 1 2 2 2


# array = {"Bob": 1, "John": 4, "Bill": 2, "Jack": 1, "Mary": 2, "Luis": 2}
# base = set()
#
#
# for i in arr:  # для каждого студента в массиве анализируем номер ID
#     if arr.get(i) not in base:  # для каждого ID  проверяем его наличие в контрольном массиве
#
#         base.add(i)
#         base.add(arr.get(i))
#         print(base)
#     else:
#         print(base)


#     base[i].append(arr[i])
#     arr[i].count = 1
# else:
#     arr[i].count += 1
#
# base.sort()  # сортируем массив
# print(base)
# max_elem = max(base)  # определяем максимальный элемент в массиве
# print(max_elem)
#
#
