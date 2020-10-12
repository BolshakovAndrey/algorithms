s = input('a b c a b c b b').split()

s = 'a b c a b c b b'


def longest_substr(s):
    longest = 0
    for start_index in range(len(s)):
        contains = set()
        for letter in s[start_index:]:
            if letter in contains:
                break
            contains.add(letter)
        longest = max(longest, len(contains))
    print('\n Длина наибольшей подстроки: -', longest)


longest_substr(s)
