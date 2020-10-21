a = int(input())
# запишем остаток от деления тут
result = []

while a:
    result.append(a % 2)
    a //= 2
# перевернем строку наоборот
result.reverse()
# Заменяем пробелы между елементами списка
# которые генерит print() на пустоту
print(sep='', *result)
