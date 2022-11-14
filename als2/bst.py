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

        found_node = BSTFind()

        if self.Root is None:
            return found_node

        def traverseTree(node: BSTNode, parentNode):
            if node is None:
                found_node.Node = parentNode
                found_node.NodeHasKey = False
                found_node.ToLeft = True if key < parentNode.NodeKey else False
                return

            if node.NodeKey == key:
                found_node.Node = node
                found_node.NodeHasKey = True
                return

            traverseTree(node.LeftChild if key < node.NodeKey else node.RightChild, node)

        traverseTree(self.Root, None)

        return found_node

    def AddKeyValue(self, key, val):
        found_node = self.FindNodeByKey(key)

        if found_node.NodeHasKey:
            return False

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        def traverseTree(node: BSTNode, parent_key):
            if node is None:
                return

            if node.NodeKey == parent_key:
                if found_node.ToLeft:
                    node.LeftChild = BSTNode(key, val, node)
                else:
                    node.RightChild = BSTNode(key, val, node)
                return

            traverseTree(node.LeftChild if parent_key < node.NodeKey else node.RightChild, parent_key)

        traverseTree(self.Root, found_node.Node.NodeKey)

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
