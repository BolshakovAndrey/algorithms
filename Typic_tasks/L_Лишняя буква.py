s = sorted(input().strip())
t = sorted(input().strip())


def left_letter(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[len(t) - 1]


print(left_letter(s, t))
