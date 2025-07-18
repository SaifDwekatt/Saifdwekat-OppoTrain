class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None
