class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def display(self, limit=10):
        if not self.head:
            print("List is empty")
            return
        result = []
        curr = self.head
        count = 0
        while curr and count < limit:
            result.append(curr.value)
            curr = curr.next
            count += 1
            if curr == self.head:
                break
        print("Circular List:", result)

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.display()
