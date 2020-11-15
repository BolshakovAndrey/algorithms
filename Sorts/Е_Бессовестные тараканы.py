"""
Номер успешной отправки - 40504951
"""
from collections import Counter


def solution(array1, array2):
    res = []
    hash_list = Counter(array2)
    for i in array1:
        if hash_list[i] > 0:
            res.append(i)
            hash_list[i] -= 1
    return res


if __name__ == '__main__':
    first_len = int(input())
    second_len = int(input())
    if first_len > 0:
        first_arr = [i for i in (input().split(" "))]
    else:
        first_arr = []

    if second_len > 0:
        second_arr = [p for p in (input().split(" "))]

    else:
        second_arr = []
    answer = solution(first_arr, second_arr)
    print(*answer)
