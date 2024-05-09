class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError('Capacity cannot be a negative number')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return  self.size * '🍪'

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('Limit Exceeded')
        if self.size + n > self.capacity:
            raise ValueError('Limit Exceeded')
        self.size += n
        return self
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError('Not enough cookies')
        self.size -= n
        return self

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

# Example usage:
jar = Jar()
print(jar)
jar.deposit(3)
print(jar)
jar.withdraw(2)
print(jar)
