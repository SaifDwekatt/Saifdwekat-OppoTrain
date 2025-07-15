class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = value
        self._size += 1

    def _resize(self):
        self._capacity *= 2
        new_array = self._make_array(self._capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def get(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        raise IndexError("Index out of bounds")

    def __len__(self):
        return self._size

    def __str__(self):
        return str([self._array[i] for i in range(self._size)])
