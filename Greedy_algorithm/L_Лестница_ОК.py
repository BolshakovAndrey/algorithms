"""
Номер успешной отправки - 41058839  15 ноя 2020, 14:22:08
"""
n = int(input())
stairs = [int(i) for i in input().split()]
step = 1
for i in range(n - 2, -1, -1):
    if stairs[i] < step:
        step += 1
    else:
        step = 1
if step == 1:
    print(True)
else:
    print(False)
