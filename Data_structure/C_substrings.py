s = list(input())


# def longest_substr(s):
#     longest = 0
#     for start_index in range(len(s)):
#         contains = set()
#         for letter in s[start_index:]:
#             if letter in contains:
#                 break
#             contains.add(letter)
#         longest = max(longest, len(contains))
#     return print(longest)
#
#
# longest_substr(s)

result = 0
while len(s) != 0:
    intermediate = ''

    for letter in s:
        if letter not in intermediate:
            intermediate += letter
        else:
            if len(intermediate) > result:
                result = len(intermediate)
            s = s[s.index(letter) + 1:]
            break

    if intermediate == s:
        s = ''
        if len(intermediate) > result:
            result = len(intermediate)


print(result)