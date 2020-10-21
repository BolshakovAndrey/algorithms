#  успешная отправка 36946310 - 19 окт 2020, 11:28:24
n = int(input())
# Считаем строку
input_string = [str(a) for a in input().split(' ')]

counter = {}
for elem in input_string:
    counter[elem] = counter.get(elem, 0) + 1
doubles = {element: count for element, count in counter.items() if count != 2}

print("".join(doubles.keys()))