# Номер посылки - 35782323 10 окт 2020, 23:33:04


import unittest


class Stack:
    """Create stack"""

    def __init__(self):
        """
        In the constructor, create an empty list for the class instance.

        """
        self.items = []

    def isempty(self):
        """
        Check the stack is empty.
        """
        return self.items == []

    def push(self, item):
        """
        Adds an element to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Delete items.
        """
        return self.items.pop()

    def peak(self):
        """
        Returns an element from the top of the stack (without deleting).
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Returns the stack size.
        """
        return len(self.items)


def calculator(input_str):
    """
    Returns the result of a calculated expression written in
    Reverse Polish Notation (RPN).
    """

    # Operations can be submitted to the input: +, -, *, /
    # The division operation is integer. That is, for example, 12 5 / will be 2.

    action = {
        '+': float.__add__,
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__floordiv__,
    }

    stack = Stack()
    ops = action.keys()

    for symbol in input_str.split():
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
                    # print('Not enough operands')
                    raise
                try:
                    operand = action[operand](operand1, operand2)
                except ZeroDivisionError:
                    # print("You can't divide by zero")
                    raise
                stack.push(operand)

    if stack.size() != 1:
        # print('Too many operands')
        raise
    return stack.pop()


input_string = input()
res = calculator(input_string)
print(int(res))


class OKTest(unittest.TestCase):
    """Tests"""

    def runTest(self):
        """
        Testing sample data and additional data
        erroneous and extreme data
        """
        self.assertEqual(1, calculator("1"))
        self.assertEqual(9, calculator("2 1 + 3 *"))
        self.assertEqual(38, calculator("7 2 + 4 * 2 +"))
        self.assertEqual(-0.5, calculator("2.0 3.5 + 6 -"))
        self.assertEqual(14, calculator("5 1 2 + 4 * 3 -+"))
        self.assertEqual(9999, calculator("-1 10000 +"))
        with self.assertRaises(IndexError):  # Not enough operands
            calculator("+")
        with self.assertRaises(ZeroDivisionError):  # You can't divide by zero
            calculator("2 0 /")


if __name__ == "__main__":
    unittest.main()
