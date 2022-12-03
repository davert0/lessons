class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a
        a = sorted(a)
        middle_index = len(a) // 2
        middle_key = a[middle_index]
        self.Root = BSTNode(middle_key, None)
        self.generate(self.Root, a[:middle_index], 1)
        self.generate(self.Root, a[middle_index:], 1)
        return self.Root

    def generate(self, parent, a, level):
        if not a:
            return
        if len(a) == 1:
            node = BSTNode(a[0], parent)
            node.Level = level
            if node.NodeKey < parent.NodeKey:
                parent.LeftChild = node
            if node.NodeKey > parent.NodeKey:
                parent.RightChild = node
            return
        middle_index = len(a) // 2
        middle_key = a[middle_index]
        node = BSTNode(middle_key, parent)
        if node.NodeKey < parent.NodeKey:
            parent.LeftChild = node
            print(node.NodeKey)
        if node.NodeKey > parent.NodeKey:  # 3 5 8 10 12 15 18
            parent.RightChild = node
        node.Level = level
        node.LeftChild = self.generate(node, a[:middle_index], level + 1)
        node.RightChild = self.generate(node, a[middle_index:], level + 1)

    def IsBalanced(self, root_node):
        return False
