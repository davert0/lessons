from time import process_time_ns


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
        
class PowerSet(HashTable):

    def __init__(self, sz, stp):
        super().__init__(sz, stp)
        self.slots = dict()

    def hash_fun(self, value):
        return hash(value)

    def size(self):
        return len(self.slots)

    def put(self, value):
        self.slots[value] = value

    def get(self, value):
        return value in self.slots

    def remove(self, value):
        return bool(self.slots.pop(value, False))

    def intersection(self, set2):
        intersect_set = PowerSet()
        for slot in self.slots:
            if slot in set2.slots:
                intersect_set.put(self.slots[slot])
        return intersect_set

    def union(self, set2):
        union_set = PowerSet()
        slots = self.slots
        for slot in set2.slots:
            slots[slot] = slot
        union_set.slots = slots
        return union_set

    def difference(self, set2):
        difference_set = PowerSet()
        for slot in self.slots:
            if slot not in set2.slots:
                difference_set.put(slot)
        return difference_set

    def issubset(self, set2):
        return all([slot in self.slots for slot in set2.slots])