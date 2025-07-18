class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":
    q = QueueArray()
    q.enqueue(1)
    q.enqueue(2)
    print("Queue:", q)
    print("Dequeued:", q.dequeue())
    print("After dequeue:", q)
