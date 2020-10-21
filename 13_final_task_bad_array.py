""" Успешная отправка 37325675  20 окт 2020, 23:01:15 """

n = int(input())
k = int(input())
arr = [int(a) for a in input().split(' ')]


def search(bad_array, n, key):
    """
    Searching for an element in an unsorted python array
    :param bad_array: type(int) A string separated by a space.
    :param n: The length of the array
    :param key: A positive number k is the desired element.
    :return: Index of the searched if it is found. Otherwise, -1.
    """
    for i in range(n):
        if bad_array[i] == key:
            return i
    return -1


index = search(arr, n, k)
print(index)
