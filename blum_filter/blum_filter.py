

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0b0


    def hash1(self, str1):
        # 17
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 17 + code) % self.filter_len
        return result

    def hash2(self, str1):
        # 223
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % self.filter_len
        return result

    def add(self, str1):
        hash1 = 0b1 << self.hash1(str1)
        hash2 = 0b1 << self.hash2(str1)
        self.filter = self.filter | hash1
        self.filter = self.filter | hash2

    def is_value(self, str1):
        hash1 = 0b1 << self.hash1(str1)
        hash2 = 0b1 << self.hash2(str1)
        return (self.filter | hash1) == self.filter and (self.filter | hash2) == self.filter