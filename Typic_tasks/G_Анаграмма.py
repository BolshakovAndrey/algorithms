from collections import Counter


def count(string):
    temp = list(string)
    collection = Counter()
    for word in temp:
        collection[word] += 1
    return collection


first = "мошкара"
second = "ромашка"

print(1 if count(first) == count(second) else 0)