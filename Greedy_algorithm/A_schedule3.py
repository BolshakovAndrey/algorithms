def schedule(lessons):
    result = []
    lst = sorted(lessons, key=lambda x: (float(x[1]), float(x[0])))
    while len(lst) > 0:
        right = lst[0][1]
        result.append(lst[0])
        while len(lst) > 0 and lst[0][0] < right:
            del lst[0]
    return result


n = int(input())
lessons_lst = []

while len(lessons_lst) != n:
    a = str(input()).split()
    lessons_lst.append(a)

print('\n'.join(schedule(lessons_lst)))