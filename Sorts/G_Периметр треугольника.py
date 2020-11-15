"""
Номер успешной отправки - 41064380  15 ноя 2020, 15:28:27
"""
def solution(array):
    array.sort(reverse=True)
    index = 0
    while arr_len - 3 >= index:
        amount = array[index] + array[index + 1] + array[index + 2]
        if amount - array[index] > array[index]:
            return amount
        index += 1


if __name__ == '__main__':
    arr_len = int(input())
    if arr_len > 0:
        arr = [int(i) for i in (input().split(" "))]
    else:
        arr = []
    answer = solution(arr)
    print(answer)