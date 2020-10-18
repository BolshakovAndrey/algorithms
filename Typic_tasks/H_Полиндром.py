# номер успешной отправки 36307707 14 окт 2020, 15:14:36
s = input().lower()
new = ''
for i in s:
    if i.isalpha() and not i.isnumeric():
        new += i
if new == new[::-1]:
    print("True")
else:
    print("False")
