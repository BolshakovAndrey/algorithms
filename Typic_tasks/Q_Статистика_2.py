lenghtArray = input()

array = list(map(int, input().split(' ')))


negative = []
positive = list()
count = 0

for item in array:
    negative.append(item) if item < 0 else positive.append(item)
    count += 1

negative = sorted(negative)
positive = sorted(positive, reverse=True)
result = 0

for numPos in positive:
    for i in range(len(negative)):
        for j in range(i, len(negative) - i):
            count += 1
            my_sum = numPos + negative[i] + negative[j]
            my_product = numPos * negative[i] * negative[j]
            if (my_sum == 0 and (
                    my_product % 2 == 0) and my_product > 0 and my_product > result):
                result = my_product

print(result if result != 0 else -1)
