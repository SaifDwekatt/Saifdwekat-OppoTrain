class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display_forward(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        print("Forward:", result)

    def display_backward(self):
        result = []
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        while curr:
            result.append(curr.value)
            curr = curr.prev
        print("Backward:", result)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display_forward()
    dll.display_backward()
