class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        tree_size = 2 * 2**depth - 1
        self.HeapArray = [None] * tree_size
        if not a:
            return []
        for i in a:
            self.Add(i)
        return self.HeapArray

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1

        max = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[-1]
        self.HeapArray[-1] = None

        self.Restruct(0)

        return max

    def Restruct(self, index):
        left_child_index = self.GetLeftChildIndex(index)
        right_child_index = self.GetRightChildIndex(index)
        if left_child_index >= len(self.HeapArray) and right_child_index >= len(
            self.HeapArray
        ):
            return
        current_element = self.HeapArray[index]
        left_child = self.HeapArray[left_child_index]
        right_child = self.HeapArray[right_child_index]
        if left_child < current_element and right_child < current_element:
            return

        if left_child > current_element and right_child > current_element:
            next_index = (
                left_child_index if left_child > right_child else right_child_index
            )
        if left_child > current_element > right_child:
            next_index = left_child_index
        if left_child < current_element < right_child:
            next_index = right_child_index

        self.HeapArray[index], self.HeapArray[next_index] = (
            self.HeapArray[next_index],
            self.HeapArray[index],
        )

        self.Restruct(next_index)

    def GetLeftChildIndex(self, index):
        return 2 * index + 1

    def GetRightChildIndex(self, index):
        return 2 * index + 2

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if None not in self.HeapArray:
            return False
        index = self.HeapArray.index(None)
        self.HeapArray[index] = key
        if index == 0:
            return True
        parent_index = (index - 1) // 2
        while self.HeapArray[parent_index] < key:
            self.HeapArray[index] = self.HeapArray[parent_index]
            self.HeapArray[parent_index] = key
            index = parent_index
            parent_index = (parent_index - 1) // 2
            if parent_index < 0:
                parent_index = 0

        current_index = self.HeapArray.index(key)
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2

        try:
            if (
                self.HeapArray[left_child_index] is not None
                and self.HeapArray[left_child_index] > key
            ):
                self.HeapArray[current_index] = self.HeapArray[left_child_index]
                self.HeapArray[left_child_index] = key
        except IndexError:
            pass

        try:
            if (
                self.HeapArray[right_child_index] is not None
                and self.HeapArray[right_child_index] > key
            ):
                self.HeapArray[current_index] = self.HeapArray[right_child_index]
                self.HeapArray[right_child_index] = key
        except IndexError:
            pass
