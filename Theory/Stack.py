class Stack:

    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        """
        Delete items.
        """
        # if len(self.__items) != 0:
        #     return self.__items.pop()
        # return print("Index Error: deleting from an empty stack")
        try:
            return self.__items.pop()
        except IndexError:
            print("Index Error: deleting from an empty stack")
            return


    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

stack1 = Stack()
# stack1.push("first")
print(stack1.isEmpty())
print(stack1.size())
stack1.pop()
print(stack1.size())