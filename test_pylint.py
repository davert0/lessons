class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, value):
        value = value.encode("utf-8")
        sum_bytes = 0
        for byte in value:
            sum_bytes += byte
        return sum_bytes % self.size

    def get(self, key):
        index = self.find(key)
        if index is None:
            return None
        self.hits[index] += 1
        return self.values[index]

    def put(self, key, value):
        index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def seek_slot(self, key):
        index = self.hash_fun(key)
        if not self.slots[index] or self.slots[index] == key:
            return index
        new_index = (index + 3) % self.size
        while new_index != index:
            if not self.slots[new_index] or self.slots[new_index] == key:
                return new_index
            new_index = (new_index + 3) % self.size
        if not self.slots.count(None):
            index = self.hits.index(min(self.hits))
            self.slots[index] = None
            self.values[index] = None
            return index

    def find(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return index
        new_index = (index + 3) % self.size
        while new_index != index:
            if self.slots[new_index] == key:
                return new_index
            new_index = (new_index + 3) % self.size
        return None
