n = int(input())  # В первой строке записано число n - длина массива.
k = int(input())  # Во второй строке записано положительное число k - искомый элемент.
arr = [int(a) for a in input().split(' ')]  # В строку через пробел записаны n положительных чисел


def Search(arr, k, l=0, r=len(arr) - 1):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return Search(arr, k, l, mid - 1)

        else:
            return Search(arr, k, mid + 1, r)
    else:
        return -1


res = Search(arr, k)
print(res)
