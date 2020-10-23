""" 37773815 """


def search(arr, key):
    """
    Searching for an element in an unsorted python array
    :param arr: type(int) A string separated by a space.
    :param key: A positive number k is the desired element.
    :return: Index of the searched if it is found. Otherwise, -1.
    """
    first = arr[0]
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int(left + (right - left) // 2)
        if arr[mid] == key:
            return mid
        if (arr[mid] < first) != (key < first) or (arr[mid] < key):
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    quantity = int(input())
    k = int(input())
    array = [int(a) for a in input().split(' ')]
    print(search(array, k))
