class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

print(n1.next) # second
print(n2.next) # third
print(n3.next) # None

def insert_node(node, index, value):
    head = node
    new_node = Node(value)
    if index == 0:
        new_node.next = node
        return new_node
    while index-1:
        node = node.next
        index -= 1
    tmp = node.next
    node.next = new_node
    new_node.next = tmp
    return head

node, index, value = n1, 2, 'new_node'
head = insert_node(node, index, value)

print(head) # first
print(head.next) # second
print(head.next.next) # new_node