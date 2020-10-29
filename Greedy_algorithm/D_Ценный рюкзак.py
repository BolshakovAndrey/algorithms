"""
# Номер успещной отправки 38517874 - 29 окт 2020, 12:39:42
"""
weight = int(input())
n =  int(input())

costWeight = []
for i in range(n):
    c, w = map(int, input().split())
    costWeight.append((c, w, i))

sortedWeight = sorted(costWeight, key=lambda x: (-x[0], x[1]), reverse=False)
totalCost = 0
answer = []
for tup in sortedWeight:
    if weight >= tup[1]:
        weight -= tup[1]
        totalCost += tup[0]
        answer.append(tup[2])

print(*sorted(answer))
