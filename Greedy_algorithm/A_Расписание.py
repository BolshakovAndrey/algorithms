result = []


def schedule(array):
    if len(array) == 1:
        return array

    if array[0][1] == array[1][1]:
        result.append(min(array[0], array[1]))
    else:
        result.append(array[0])

    for i in range(1, len(array) - 1):
        if array[i][0] >= result[-1][1]:
            if array[i][1] == array[i + 1][1] and array[i + 1][0] >= result[-1][1]:
                result.append(min(array[i], array[i + 1]))
            else:
                result.append(array[i])
    if array[n - 1][0] >= result[-1][1]:
        result.append(array[n - 1])
    return result


def print_result(result):
    print(len(result))
    for item in result:
        print(' '.join(
            list(map(str, map(
                lambda number: int(
                    number) if number % 1 == 0 else number, item)))))


n = int(input())
lessons = []
lessons = list(list(list(map(float, input().split(" ")))) for _ in range(n))
lessons = sorted(lessons, key=lambda x: (x[1], x[0]))
print_result(schedule(lessons))
