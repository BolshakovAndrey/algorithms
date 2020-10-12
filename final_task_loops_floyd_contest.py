# Номер успешной отправки 36139292 - 12 окт 2020, 23:37:58

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


