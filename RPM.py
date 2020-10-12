import unittest


# Создадим класс стек
class Stack:

    def __init__(self):
        """
        В конструкторе для экземпляра класса создадим пустой список.
        """
        self.items = []

    def isEmpty(self):
        """
        Определяет, пуст ли стек.
        :return:
        """
        return self.items == []

    def push(self, item):
        """
        Добавляет элемент на вершину стека.
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        Удаляет элемент.
        :return:
        """
        return self.items.pop()

    def peak(self):
        """
        Возвращает элемент из вершины стека (без удаления).
        :return:
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Возвращает размер стека.
        :return:
        """
        return len(self.items)


def calculator(input_string):
    """
    Возвращает результат вычисленного выражения записанного в виде обратной
    польской нотации
    """

    # На вход могут подаваться операции: +, -, *, /
    # Операция деления целочисленная. То есть, например, 12 5 / будет 2.

    OPERATORS = {
        '+': float.__add__,
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__floordiv__,
    }

    stack = Stack()
    ops = OPERATORS.keys()

    for symbol in input_string.split():
        try:
            symbol = float(symbol)
            stack.push(symbol)
        except ValueError:
            for operand in symbol:
                if operand not in ops:
                    continue
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()

                except IndexError:
                    raise Exception('Не хватает операндов')

                try:
                    operand = OPERATORS[operand](operand1, operand2)
                except ZeroDivisionError:
                    raise Exception("На ноль делить нельзя")

                stack.push(operand)

    if stack.size() != 1:
        raise Exception('Слишком много операндов')
    return stack.pop()


res1 = calculator("2 1 + 3 *")
print(res1)
res2 = calculator("7 2 + 4 * 2 +")
print(res2)


class TestRPN(unittest.TestCase):
    def runTest(self):
        self.assertEqual(9, calculator("2 1 + 3 *"))
        self.assertEqual(38, calculator("7 2 + 4 * 2 +"))


if __name__ == "__main__":
    unittest.main()
