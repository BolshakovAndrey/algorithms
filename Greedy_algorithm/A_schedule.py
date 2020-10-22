"""
1.Выбрать урок, который завершается раньше остальных. Он будет первым в списке.
2.Выбрать предмет, который начинается после окончания первого.
При этом он должен заканчиваться раньше всех прочих, которые удовлетворяют первому условию.
Такой урок окажется вторым в списке.
"""


def timetable():
    """
    Collect and prepare data
    :return: float timetable
    """
    number = int(input())
    lessons_times = []
    float_times = []
    for i in range(0, number):
        line = (input().split())
        lessons_times.append(line)

    for item in lessons_times:
        lst = [float(i) for i in item]
        float_times.append(lst)
    res = sorted(float_times)
    return res


result = []


def schedule(data):
    while len(data) > 0:
        right = data[0][1]
        result.append(data[0])
        while len(data) > 0 and data[0][0] < right:
            del data[0]
    return result


def printResult(array):
    print(len(array))
    for item in array:
        print(' '.join(list(map(str, map(lambda number: int(number) if number % 1 == 0 else number, item)))))


printResult(schedule(timetable()))


