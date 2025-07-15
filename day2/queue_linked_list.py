class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        val = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def peek(self):
        return self.front.value if self.front else None

    def is_empty(self):
        return self.front is None

if __name__ == "__main__":
    q = QueueLinkedList()
    q.enqueue("A")
    q.enqueue("B")
    print("Peek:", q.peek())
    print("Dequeued:", q.dequeue())
