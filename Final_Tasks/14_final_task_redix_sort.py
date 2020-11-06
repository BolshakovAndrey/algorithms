# Номер  успешной отправки - 39300502 - 4 ноя 2020, 22:25:22
n = int(input())
arr = [p for p in input().split(' ')]

# max_len — number of digits in the longest key;
max_len = len(max(arr, key=len))

# Use an iterative approach based on LSD - it's faster

sort_arr = arr[:]
for exponent in range(max_len):
    digits = [[] for i in range(10)]  # create buckets for each digit
    index = -(exponent + 1)  # get the string index for the number

    for number in sort_arr:  # placing numbers into a bucket based on LSD
        string_number = str(number)
        try:
            digit = int(string_number[index])  # getting digit at current place
        except IndexError:
            digit = 0  # if number doesn't have this digit it is 0
        digits[digit].append(number)

    sort_arr = []
    for numeral in digits:
        sort_arr.extend(numeral)

print(*sort_arr)
