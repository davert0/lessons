class PowerSet:
    def __init__(self, *args, **kwargs):
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
        for key in self.slots:
            union_set.put(key)
        for key in set2.slots:
            union_set.put(key)
        return union_set


    def difference(self, set2):
        difference_set = PowerSet()
        for slot in self.slots:
            if slot not in set2.slots:
                difference_set.put(slot)
        return difference_set

    def issubset(self, set2):
        return all([slot in self.slots for slot in set2.slots])