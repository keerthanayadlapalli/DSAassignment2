class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s1 and not self.s2:
            return -1
        if self.s2:
            return self.s2.pop()
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s1 and not self.s2:
            return -1
        if self.s2:
            return self.s2[-1]
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Example usage
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())   # Output: 1
print(queue.pop())    # Output: 1
print(queue.empty())  # Output: False
