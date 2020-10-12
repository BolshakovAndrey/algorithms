class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def print_list(node):
    while node:
        print(node),
        node = node.next_item
    print()


node3 = Node('third')
node2 = Node('second', node3)
node1 = Node('first', node2)
node = Node("test", node1)
print(node)

print_list(node)
