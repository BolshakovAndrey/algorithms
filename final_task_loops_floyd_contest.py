# Номер посылки 35898329 - 12 окт 2020, 13:44:55

class Node(object):

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
    if not head:
        return False
    hare, tortoise = head, head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            return True
    return False
