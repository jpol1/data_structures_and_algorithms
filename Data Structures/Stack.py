class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def get_size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[len(self.stack)-1]