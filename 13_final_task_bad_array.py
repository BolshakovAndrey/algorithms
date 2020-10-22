""" 37773431 """


def search(arr, k):
    """
    Searching for an element in an unsorted python array
    :param arr: type(int) A string separated by a space.
    :param k: A positive number k is the desired element.
    :return: Index of the searched if it is found. Otherwise, -1.
    """
    first = arr[0]
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int(left + (right - left) // 2)
        if arr[mid] == k:
            return mid
        elif (arr[mid] < first) != (k < first) or (arr[mid] < k):
            left = mid + 1
        else:
            right = mid - 1
    return -1


n = int(input())
k = int(input())
array = [int(a) for a in input().split(' ')]
print(search(array, k))
