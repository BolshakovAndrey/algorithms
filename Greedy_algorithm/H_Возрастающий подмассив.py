# n - число элементов массива
# arr -в строку записаны n чисел

n = int(input())
arr = [int(p) for p in input().split(" ")]
sort_arr = sorted(arr)
res = set(sort_arr)
answer = len(res)
print(answer)


