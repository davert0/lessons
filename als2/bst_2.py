class aBST:

    def __init__(self, depth):
        tree_size = 1
        if depth > 0:
            for i in range(1, depth+1):
                tree_size += 2**i
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        index = 0
        
        while index < len(self.Tree):
            node = self.Tree[index]
            if key == node:
                return index
            if key < node:
                index = 2 * index + 1
            if key > node:
                index = 2 * index + 2      

        return None 
	
    def AddKey(self, key):
        index = 0
        while index < len(self.Tree):
            node = self.Tree[index]
            if node is None:
                self.Tree[index] = key
                return index
            if key == node:
                return index
            if key < node:
                index = 2 * index + 1
            if key > node:
                index = 2 * index + 2  
        return -1; 
        # индекс добавленного/существующего ключа или -1 если не удалось3