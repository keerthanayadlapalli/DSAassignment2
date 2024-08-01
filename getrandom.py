import random

class RandomizedSet:
    def __init__(self):
        self.v = []
        self.mp = {}

    def search(self, val: int) -> bool:
        return val in self.mp

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.v.append(val)
        self.mp[val] = len(self.v) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        idx = self.mp[val]
        last_element = self.v[-1]
        self.v[idx] = last_element
        self.v.pop()
        self.mp[last_element] = idx
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)

# Example usage
random_set = RandomizedSet()
random_set.insert(1)
random_set.insert(2)
print(random_set.remove(1))   # Output: True
print(random_set.insert(2))   # Output: False
print(random_set.getRandom()) # Output: Random element from the set
