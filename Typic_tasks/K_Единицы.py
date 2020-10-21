# Номер успешной отправки 36963127 - 19 окт 2020, 12:29:23

n = int(input())
b = bin(n)

count = 0
for i in b:
    if i == '1':
        count += 1
print(count)