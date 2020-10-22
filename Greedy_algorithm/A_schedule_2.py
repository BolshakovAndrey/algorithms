import operator
filename = 'timetable.txt'

array = []

def printResult(array):
    lenght = len(array)
    print(lenght)

    for item in array:
        print(' '.join(list(map(str, map(lambda number: int(number) if number % 1 == 0 else number, item)))))

with open(filename, 'r') as f:
    number = int(f.readline())

    for i in range(number):
        line = f.readline()
        array.append(list(map(float, line.strip().split())))


def timetable(array):
    array = sorted(array, key=operator.itemgetter(1, 0))
    result = []
    print(array)

    if len(array) == 1:
        return array


    if array[0][1] == array[1][1]:
        result.append(min(array[0], array[1]))
    else:
        result.append(array[0])

    for i in range(1, len(array) - 1):

        if array[i][0] >= result[-1][1]:
            if array[i][1] == array[i+1][1] and array[i+1][0] >= result[-1][1]:
                result.append(min(array[i], array[i+1]))
            else:
                result.append(array[i])

    if array[number - 1][0] >= result[-1][1]:
        result.append(array[number - 1])

    return result


printResult(timetable(array))