class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def dont_have_children(self):
        return self.LeftChild is None and self.RightChild is None


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        if node is not None:
            node.Parent = None

    def FindNodeByKey(self, key):
        res = BSTFind()
        if self.Root is None:
            res.Node = self.Root
            res.NodeHasKey = False
            res.ToLeft = False
            return res
        elif self.Root.NodeKey == key:
            res.Node = self.Root
            res.NodeHasKey = True
            res.ToLeft = False
            return res
        elif key > self.Root.NodeKey:
            if self.Root.RightChild is not None:
                return BST(self.Root.RightChild).FindNodeByKey(key)
            else:
                res.Node = self.Root
                res.NodeHasKey = False
                res.ToLeft = False
                return res
        else:
            if self.Root.LeftChild is not None:
                return BST(self.Root.LeftChild).FindNodeByKey(key)
            else:
                res.Node = self.Root
                res.NodeHasKey = False
                res.ToLeft = True
                return res

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        parent_node = self.FindNodeByKey(key)
        if parent_node.NodeHasKey:
            return False  # если ключ уже есть
        elif parent_node.Node is None:
            node = BSTNode(key, val, parent_node.Node)
            self.Root = node
            return True
        node = BSTNode(key, val, parent_node.Node)
        if parent_node.ToLeft:
            parent_node.Node.LeftChild = node
        else:
            parent_node.Node.RightChild = node
        return True

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode if FromNode else self.Root
        if not node:
            return None
        child = node.RightChild if FindMax else node.LeftChild
        if not child:
            return node
        return self.FinMinMax(child, FindMax)

    def recursive_delete(self, key, recursive_level):
        if self.Root is None:
            return False
        if key < self.Root.NodeKey:
            self.Root.LeftChild = BST(self.Root.LeftChild).recursive_delete(
                key, recursive_level=recursive_level + 1
            )
        elif key > self.Root.NodeKey:
            self.Root.RightChild = BST(self.Root.RightChild).recursive_delete(
                key, recursive_level=recursive_level + 1
            )
        else:
            if (
                recursive_level == 0
                and self.Root.LeftChild is None
                and self.Root.RightChild is None
            ):
                temp = self.Root
                self.Root = None
                return temp
            if self.Root.LeftChild is None:
                temp = self.Root.RightChild
                self.Root = None
                return temp
            elif self.Root.RightChild is None:
                temp = self.Root.LeftChild
                self.Root = None
                return temp

            temp = self.FinMinMax(self.Root.RightChild, FindMax=False)

            self.Root.NodeKey = temp.NodeKey

            self.Root.RightChild = BST(self.Root.RightChild).recursive_delete(
                temp.NodeKey, recursive_level=recursive_level + 1
            )

        return self.Root

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False
        return self.recursive_delete(key, 0)

    def Count(self):
        if self.Root is None:
            return 0
        return 1 + BST(self.Root.LeftChild).Count() + BST(self.Root.RightChild).Count()
