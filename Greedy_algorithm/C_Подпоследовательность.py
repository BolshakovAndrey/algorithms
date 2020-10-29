# Рекурсивная программа чтобы проверить,
# является ли строка подпоследовательностью другой строки


# def isSubSequence(string1, string2, len_str1, len_str2):
#     # Базовые случаи
#     if len_str1 == 0:
#         return True
#     if len_str2 == 0:
#         return False
#
#     # Если последние символы двух строк совпадают
#     if string1[len_str1 - 1] == string2[len_str2 - 1]:
#         return isSubSequence(string1, string2, len_str1 - 1, len_str2 - 1)
#
#     # Если последние символы не совпадают
#     return isSubSequence(string1, string2, len_str1, len_str2 - 1)
#
#
# string1 = list(input())
# string2 = list(input())
# len_str1 = len(string1)
# len_str2 = len(string2)
#
#
# if isSubSequence(string1, string2, len_str1, len_str2):
#     print("True")
# else:
#     print("False")


"""
Итеративная программа Python для проверки, является ли строка подпоследовательностью другой строки


Возвращает true, если str1 является подпоследовательностью str2
m длина str1, n длина str2
"""


# Номер успешной отправки - 38292329


def isSubSequence(str1, str2, m, n):
    j = 0  # Индекс str1
    i = 0  # Индекс str2

    # Пройдите как str1, так и str2
    # Сравнить текущий символ str2 с
    # первый непревзойденный символ str1
    # Если соответствует, то двигаться вперед в str1

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1
    # Если все символы строки str1 совпадают, то j равно m
    return j == m


str1 = list(input())
str2 = list(input())
m = len(str1)
n = len(str2)

print("True" if isSubSequence(str1, str2, m, n) else "False")
