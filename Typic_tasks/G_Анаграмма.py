# успешная  отправка 36910036 - 18 окт 2020, 21:44:34
# вариант без сторонних модулей

first = [str(x) for x in input() if x.isalpha()]
second = [str(x) for x in input() if x.isalpha()]


def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter


print("True" if count(first) == count(second) else "False")


# используем Counter
# from collections import Counter

# first = "мошкара"
# second = "ромашка"

# def count(string):
#     temp = list(string)
#     collection = Counter()
#     for word in temp:
#         collection[word] += 1
#     return collection




