# Номер успешной посылки 36138548 - 12 окт 2020, 23:15:24

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


def hasCycle(head):
    """
    Here is cycle detection algorithm
    :type head: Node
    :return type: bool
    """
    hare, tortoise = head, head
    while hare is not None and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare is tortoise:
            return True
    return False


