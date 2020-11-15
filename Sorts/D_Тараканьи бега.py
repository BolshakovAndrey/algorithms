"""
Номер успешной отправки - 40338929
"""


def solution(array1, array2):
    set_first_arr = set(first_arr)
    set_second_arr = set(second_arr)
    res = []
    for i in array1:
        if i in set_first_arr:
            set_first_arr.remove(i)
            if i in array2:
                res.append(i)
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
