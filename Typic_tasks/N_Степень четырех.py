# Номер успешной отправки - 38045326
# моя версия алгоритма через уменьшение числа до степени 4
number = int(input())
degree = 4

while degree < number:
    number = number / degree

if number % 4 == 0 or number == 1:
    print("True")
else:
    print("False")


# Можно также через увеличение числа до искомого
# number = int(input())
# degree = 4
#
# while degree < number:
#     result = degree * 4
#
# if degree == number or number == 1:
#     print(True)
# else:
#     print(False)