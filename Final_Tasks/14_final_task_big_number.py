""" Успешная отправка 39425212 - 6 ноя 2020, 20:31:10"""


class Comparator(str):
    """
    Compares the array elements
    """
    def __lt__(self, other):
        return self + other > other + self


def max_number(array):
    array.sort(key=Comparator)
    return ''.join(array)


if __name__ == '__main__':
    n = int(input())
    arr = [str(a) for a in input().split(" ")]
    print(max_number(arr))
