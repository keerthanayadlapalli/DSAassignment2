class MyStack:
    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.pop(0))
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        return self.que1.pop(0)

    def top(self) -> int:
        return self.que1[0]

    def empty(self) -> bool:
        return len(self.que1) == 0

# Example usage
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
