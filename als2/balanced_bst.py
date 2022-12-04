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
<<<<<<< HEAD
	# создаём дерево с нуля из неотсортированного массива a

        a = sorted(a)
        self.generate(a, None, 0)
=======
        # создаём дерево с нуля из неотсортированного массива a
        a = sorted(a)
        middle_index = len(a) // 2
        middle_key = a[middle_index]
        self.Root = BSTNode(middle_key, None)
        self.generate(self.Root, a[:middle_index], 1)
        self.generate(self.Root, a[middle_index:], 1)
>>>>>>> 151d708362416ed79a6d0d08025fa3343214c58c
        return self.Root

    def generate(self, a, parent, level):
        if not a:
            return None
        if len(a) == 1:
<<<<<<< HEAD
            self.Root = BSTNode(a[0], parent)
            self.Root.Level = level
            return self.Root
        middle_index = len(a)//2
        root_key = a[middle_index]
        self.Root = BSTNode(root_key, parent)
        self.Root.Level = level
        self.Root.LeftChild = BalancedBST().generate(a[:middle_index], self.Root, level+1)
        self.Root.RightChild = BalancedBST().generate(a[middle_index:], self.Root, level+1)
        return self.Root
=======
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
>>>>>>> 151d708362416ed79a6d0d08025fa3343214c58c

    def IsBalanced(self, root_node):
        return False
