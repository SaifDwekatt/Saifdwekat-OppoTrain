class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]

    def __str__(self):
        return str(self.table)

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Saif")
    ht.insert("age", 25)
    ht.insert("name", "Updated Saif")
    print("HashTable:", ht)
    print("Get name:", ht.get("name"))
    ht.remove("age")
    print("After removal:", ht)
