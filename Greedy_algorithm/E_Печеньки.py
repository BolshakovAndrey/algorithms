# Номер успешной отправки - 38661471
# n_children - количество детей
# greed - фактор жадности для каждого ребенка через пробел
# n_cookies - количество печенек.
# size чисел, разделенных пробелом - размеры печенек


n_children = int(input())
greed = [int(p) for p in input().split(' ')]
children = sorted(greed, reverse=True)
n_cookies = int(input())
size = [int(p) for p in input().split(' ')]
cookies = sorted(size, reverse=True)

happy_child = 0
count = 0
l_ch = len(children)
l_co = len(cookies)
i = 0
j = 0

while i < l_ch and j < l_co:
    if children[i] <= cookies[j]:
        i += 1
        happy_child += 1
    else:
        i += 1
        continue
    j += 1

print(happy_child)
