phone = {
    "2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'
}
string = str(input())

result = []

for char in string:
    if not result:
        result = list(map(str, phone[char]))
        continue

    letters = phone[char]
    temp_res = []

    for letter in result:
        for previous in letters:
            temp_res.append(letter + previous)

    result = temp_res
print(' '.join(result))