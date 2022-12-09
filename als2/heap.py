class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        tree_size = 2 * 2**depth - 1
        self.HeapArray = [None] * tree_size
        for i in a:
            self.Add(i)
        return self.HeapArray

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if None not in self.HeapArray:
            return False
        index = self.HeapArray.index(None)
        parent_index = (index-1)//2
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        self.HeapArray[index] = key
        if index == 0:
            return True

        while self.HeapArray[index-1] is not None and key > self.HeapArray[parent_index]:
            self.HeapArray[index] = self.HeapArray[parent_index]
            self.HeapArray[parent_index] = key
            index = index-1

        


"""
Аналогично выполняется и процесс вставки. 
Новый элемент помещаем в самый низ массива, в первый свободный слот, и затем поднимаем его вверх по дереву, 
останавливаясь в позиции, когда выше у родителя будет больший ключ, а ниже у обоих наследников -- меньшие.
"""
# while index < len(self.Tree):
#     node = self.Tree[index]
#     if node is None:
#         self.Tree[index] = key
#         return index
#     if key == node:
#         return index
#     if key < node:
#         index = 2 * index + 1
#     if key > node:
#         index = 2 * index + 2
# return -1
