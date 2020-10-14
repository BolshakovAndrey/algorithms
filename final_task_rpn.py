# Номер успешной посылки 36300628 14 окт 2020, 14:38:13

ACTION = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


class Stack:
    """Create stack"""

    def __init__(self):
        """
        In the constructor, create an empty list for the class instance.
        """
        self.__items = []

    def push(self, item):
        """
        Adds an element to the top of the stack.
        """
        self.__items.append(item)

    def pop(self):
        """
        Delete items.
        """
        try:
            return self.__items.pop()
        except IndexError:
            print("Index Error: deleting from an empty stack")


def calculator(input_string):
    """
    Returns the result of a calculated expression written in
    Reverse Polish Notation (RPN).
    """

    stack = Stack()
    ops = ACTION.keys()

    for symbol in input_string:
        try:
            symbol = float(symbol)
            stack.push(symbol)
        except ValueError:
            for operand in symbol:
                if operand not in ops:
                    stack.push(int(operand))
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                except IndexError:
                    raise
                try:
                    operand = ACTION[operand](operand1, operand2)
                except ZeroDivisionError:
                    raise
                stack.push(operand)
    return stack.pop()


input_data = input().split()
res = calculator(input_data)
print(int(res))
