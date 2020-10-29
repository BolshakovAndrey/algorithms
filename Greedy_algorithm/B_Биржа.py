# Номер успешной отправки - 38139402
n = int(input())
arr = [int(p) for p in input().split(' ')]
summ = 0

for d in range(1, len(arr)):
    if arr[d] > arr[d-1]:
        tmp = arr[d] - arr[d-1]
        summ += tmp
print(summ)
