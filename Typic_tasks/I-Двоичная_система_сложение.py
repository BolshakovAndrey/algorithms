# Успешная отправка 36916191 - 19 окт 2020, 00:04:17

a = input()
b = input()


def add(a, b):
    """
    функция выполняет двоичное сложение и возвращает результат в виде строки
    :param a: type(str)
    :param b: type(str)
    :return: type(str)
    """
    maxlen = max(len(a), len(b))

    # Нормализация длины
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)

    result = ''
    carry = 0
    for i in range(maxlen - 1, -1, -1):  # обратный порядок, уменьшающийся на 1 в каждой итерации
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0: result = '1' + result
    result.zfill(maxlen)
    return result[-maxlen - 10:]


# Запускаем
res = add(a, b)
print(res)
