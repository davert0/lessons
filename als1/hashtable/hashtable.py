class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        value = value.encode("utf-8")
        sum_bytes = 0
        for byte in value:
            sum_bytes += byte
        return sum_bytes % self.size

    def seek_slot(self, value):
        if not self.slots.count(None):
            return None
        index = self.hash_fun(value)
        if not self.slots[index]:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if not self.slots[new_index]:
                return new_index
            new_index = (new_index + self.step) % self.size
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if self.slots[new_index] == value:
                return new_index
            new_index = (new_index + self.step) % self.size
        return None
