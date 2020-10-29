# Решение 2 не верное хотя  считает только последовательные тройки

# n = int(input())
# arr = [int(a) for a in input().split(' ')]
# #
# # result = -1
#
# # Ищем в последовательных тройках
# for i in range(len(arr) - 2):
#     # начиная с
#     start = i + 1
#     # пока есть элементы
#     end = len(arr) - 1
#
#     my_sum = arr[start] + arr[end] + arr[i]
#     while start < end:
#         if my_sum > 0:
#             end -= 1
#         elif my_sum == 0:
#             product = arr[start] * arr[end] * arr[i]
#             start += 1
#
#             if product % 2 == 0 and product > 0 and product > 0:
#                 result = product
#         else:
#             start += 1
# print(result)





# Решение 1  мое не верное так как требовалось считать последовательные тройки.

# """
# Выведите максимальное положительное произведение
# заработанных за три дня очков среди троек дней,
# в которые их сумма равна нулю.
# Если троек, удовлетворяющих условиям, нет, нужно вывести -1.
# """
from itertools import combinations
#
n = int(input())
arr = [int(a) for a in input().split(' ')]
#
#
def multiplyList(myList):
    # Умножить элементы списка
    result = 1
    for x in myList:
        if sum(x) != 0:
            for i in x:
                result = result * x[i]
            return result


while arr:
    myList = []
    for d in arr:
        temp = multiplyList(arr[0:3:1])
        product = max(product, temp)


def findTriplets(lst, key):
    """
    Выдает список всех возможных троек из списка
    """
    res_arr = []
    def valid(val):
        res_arr.append(val)
        return res_arr
    result = list(filter(valid, list(combinations(lst, 3))))
    return result


# формируем тройки
triple = findTriplets(arr, 3)
# перемножаем тройки
product = multiplyList(triple)
# находим максмальную положительную
product = max(product, product)
print(product)
