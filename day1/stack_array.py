class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)
