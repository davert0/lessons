class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, value):
        value = value.encode("utf-8")
        sum_bytes = 0
        for byte in value:
            sum_bytes += byte
        return sum_bytes % self.size


    def is_key(self, key):
        index = self.hash_fun(key)
        return True if self.slots[index] == key else False

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None