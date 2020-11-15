"""
Номер успешной отправки - 40941990
"""


def solution(array):
    res = []
    odd = []
    even = []

    for i in array:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    count = 0
    while count < len(array) and len(res) < len(array):
        res.append(even[count])
        res.append(odd[count])
        count += 1

    return res


if __name__ == '__main__':
    arr_len = int(input())
    if arr_len > 0:
        arr = [int(i) for i in (input().split(" "))]
    else:
        arr = []
    answer = solution(arr)
    print(*answer)
