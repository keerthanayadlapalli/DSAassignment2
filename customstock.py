class CustomStack:
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(x)

    def pop(self) -> int:
        if not self.arr:
            return -1
        return self.arr.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val

# Example usage
stack = CustomStack(3) # Create a stack with a maximum size of 3
stack.push(1)          # Stack: [1]
stack.push(2)          # Stack: [1, 2]
stack.push(3)          # Stack: [1, 2, 3]
stack.push(4)          # Cannot push because the stack is full
print(stack.pop())     # Output: 3, Stack becomes: [1, 2]
stack.increment(2, 5)  # Increment first 2 elements by 5, Stack becomes: [6, 7]
print(stack.pop())     # Output: 7, Stack becomes: [6]
print(stack.pop())     # Output: 6, Stack becomes: []
print(stack.pop())     # Output: -1, Stack is empty
